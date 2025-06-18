import os
import cfbd
from cfbd.rest import ApiException
import pandas as pd
from bing_image_downloader import downloader
import re

# Configure API key authorization: ApiKeyAuth
configuration = cfbd.Configuration(access_token = 'etqv2Lq/MXukanGusNmF25paFrxTLc3If+S99JpD9dUuIBwqGpnRoT8428+FMpna')

# create an instance of the API class
api_instance1 = cfbd.GamesApi(cfbd.ApiClient(configuration))
api_instance2 = cfbd.TeamsApi(cfbd.ApiClient(configuration))
api_instance3 = cfbd.BettingApi(cfbd.ApiClient(configuration))
api_instance4 = cfbd.RankingsApi(cfbd.ApiClient(configuration))

# Function to generate outlet logo links and download missing logos if needed
def add_outlet_logos(df, base_logo_path="assets/tv-logos/"):
    # Create the new column 'outlet_logos'
    df['outlet_logos'] = df['outlet'].apply(lambda outlet: find_or_download_logo(outlet, base_logo_path))
    return df

# Helper function to sanitize folder and file names
def sanitize_filename(name):
    # Remove or replace any invalid characters
    return re.sub(r'[\\/*?:"<>|]', "", name)

# Helper function to find the logo file or download it if missing
def find_or_download_logo(outlet_name, base_path):
    folder_path = f"{base_path}{outlet_name} tv channel logo/"
    
    # Check if folder exists
    if os.path.exists(folder_path):
        # Get the first image file in the folder (assuming only one file exists)
        for file in os.listdir(folder_path):
            if file.endswith(('.png', '.jpg', '.jpeg')):  # Add extensions as necessary
                return os.path.join(folder_path, file)
    
    # If no logo exists, download it
    download_logo(outlet_name, base_path)
    
    # Recheck the folder after download
    if os.path.exists(folder_path):
        for file in os.listdir(folder_path):
            if file.endswith(('.png', '.jpg', '.jpeg')):
                return os.path.join(folder_path, file)

    # Return None if still no logo found
    return None

# Function to download logo from Wikipedia using the given downloader logic
def download_logo(outlet_name, base_path):
    downloader.download(outlet_name + " tv channel logo", limit=1, output_dir=base_path, 
                        adult_filter_off=True, force_replace=False, timeout=60, verbose=True)



def split_home_away(df):
    rows = []
    for _, row in df.iterrows():
        # Create home team row
        home_row = {
            'id': row['id'],
            'team_type': 'home',
            'team_id': row['homeId'],
            'team_name': row['homeTeam'],
            'team_conference': row['homeConference'],
            'start_date': row['startDate'],
            'venue': row['venue'],
            'neutral_site': row['neutralSite'],
            'outlet': row['outlet']
        }
        # Create away team row
        away_row = {
            'id': row['id'],
            'team_type': 'away',
            'team_id': row['awayId'],
            'team_name': row['awayTeam'],
            'team_conference': row['awayConference'],
            'start_date': row['startDate'],
            'venue': row['venue'],
            'neutral_site': row['neutralSite'],
            'outlet': row['outlet']
        }
        # Add both rows to the list
        rows.append(home_row)
        rows.append(away_row)
    
    # Return the new dataframe with two rows for each event
    return pd.DataFrame(rows)


def read_data():
    try:
        api_response_1 = api_instance1.get_games(year=2022,week=1)
        df1 = pd.DataFrame([game.to_dict() for game in api_response_1],columns=['id','startDate','neutralSite','venue','homeId','homeTeam','awayId','awayTeam','homeConference','awayConference'])
    
        api_response_2 = api_instance1.get_media(year=2022,week=1)
        df2 = pd.DataFrame([game.to_dict() for game in api_response_2],columns=['id','outlet'])

        df2['outlet'] = df2['outlet'].apply(sanitize_filename)
    
        df_init1 = pd.merge(df1, df2, on="id")
    
        modified_data = split_home_away(df_init1)
    
        api_response_3 = api_instance2.get_teams()
        
        df3 = pd.DataFrame([game.to_dict() for game in api_response_3],columns=['id','abbreviation','color','alternate_color','logos'])
    
        df3['logos'] = [x[0] if isinstance(x, list) and len(x) > 0 else '' for x in df3['logos']]
    
        df3.rename(columns={'id':'team_id'},inplace=True)
    
    
        df_init2 = pd.merge(modified_data,df3, on="team_id")
    
    
        api_response_4 = api_instance3.get_lines(year=2022,week=1)
        records = []
        for game in api_response_4:
            if game.to_dict()['lines']:  # Check if 'lines' is not empty
                last_line = game.to_dict()['lines'][-1]  # Get the last line in the lines array
                record = {
                    'id': game.to_dict()['id'],
                    'formatted_spread': last_line['formattedSpread'],
                    'over_under': last_line['overUnder']
                }
                records.append(record)
    
        df4 = pd.DataFrame(records)
    
        df_init3 = pd.merge(df_init2,df4,on="id")
    
        add_outlet_logos(df_init3)

        api_response_5 = api_instance4.get_rankings(year=2022,week=1)

        ranks_schools = []
        for item in api_response_5:
            for poll in item.to_dict()['polls']:
                for rank_info in poll['ranks']:
                    ranks_schools.append({
                        'rank': rank_info['rank'],
                        'school': rank_info['school']
                    })

        df5 = pd.DataFrame(ranks_schools)

        df5.rename(columns={'school':'team_name'},inplace=True)

        school_rank_map = dict(zip(df5['team_name'], df5['rank']))

        df_init3['rank'] = df_init3['team_name'].map(school_rank_map)
        

        return df_init3
    
    except ApiException as e:
        print("Exception: %s\n" % e)