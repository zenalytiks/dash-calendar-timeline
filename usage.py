import pandas as pd
import numpy as np
import dash
from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc
from datetime import datetime
import os
from dash_calendar_timeline import DashCalendarTimeline
from usage_banner import generate_custom_scoreboard
import base64


class CFBGuideApp:
    def __init__(self):
        self.app = dash.Dash(
            __name__,
            external_stylesheets=[dbc.themes.BOOTSTRAP],
            meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1.0"}]
        )
        self.server = self.app.server
        self.df = self._load_and_prepare_data()
        self.min_date, self.max_date = self._get_date_bounds()
        self._setup_layout()
        self._setup_callbacks()

    def _load_and_prepare_data(self):
        """Load and prepare the data with optimized column operations."""
        data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), './Fiverr Example Data v5.xlsx')
        df = pd.read_excel(data_path)
        
        # Combine date and time columns more efficiently
        df['start_time'] = pd.to_datetime(
            df['Column1.competitions.date.1'].astype(str) + " " + 
            df['Column1.competitions.date.2'].astype(str)
        )
        df['end_time'] = df['start_time'] + pd.Timedelta(hours=3, minutes=30)
        
        return df

    def _get_date_bounds(self):
        """Get min and max dates from the dataset."""
        date_col = self.df['Column1.competitions.date.1']
        return date_col.min(), date_col.max()

    def _setup_layout(self):
        """Setup the application layout."""
        self.app.layout = dbc.Container([
            dbc.NavbarSimple(
                brand="CFB Guide",
                brand_href="#",
                color="danger",
                dark=True
            ),
            dbc.Container([
                dcc.DatePickerSingle(
                    id='date-picker',
                    min_date_allowed=datetime(self.min_date.year, self.min_date.month, self.min_date.day),
                    max_date_allowed=datetime(self.max_date.year, self.max_date.month, self.max_date.day),
                    initial_visible_month=datetime(self.min_date.year, self.min_date.month, self.min_date.day),
                    date=datetime(self.min_date.year, self.min_date.month, self.min_date.day),
                    style={'zIndex': 100}
                ),
                DashCalendarTimeline(
                    id='schedule',
                    defaultTimeStart=(self.df['start_time'].astype('int64') / 10**6).min(),
                    defaultTimeEnd=(self.df['start_time'].astype('int64') / 10**6).min() + 24 * 60 * 60 * 1000,
                    sidebarWidth=100,
                    lineHeight=60,
                    itemHeightRatio=1,
                    disableScroll=True,
                    canMove=False,
                    canResize=False,
                    canChangeGroup=False,
                    sidebarHeaderVariant='left',
                    sidebarHeaderContent=html.H3("Station", className='text-center'),
                    customGroups=True,
                    customItems=True,
                ),
            ], className='pt-5')
        ], fluid=True, className='p-0')

    def _create_bins(self, df, n):
        """Create bins for data grouping."""
        x = round(len(df) / n)
        return np.array_split(df, x)

    def _get_team_data(self, game, team_idx):
        """Extract team data for a given team index (0 or 1)."""
        cols = self.df.columns
        team_cols = {
            'logo': f'Column1.competitions.competitors.team.logo',
            'color': f'Column1.competitions.competitors.team.color',
            'location': f'Column1.competitions.competitors.team.location',
            'alternate_color': f'Column1.competitions.competitors.team.alternateColor',
            'abbreviation': f'Column1.competitions.competitors.team.abbreviation',
            'rank': f'Column1.competitions.competitors.curatedRank.current'
        }
        
        team_data = {}
        for key, col in team_cols.items():
            team_data[key] = game[col].iloc[team_idx]
            if key in ['color', 'alternate_color']:
                team_data[key] = f"#{team_data[key]}"
        
        # Add rank to location if ranked
        if team_data['rank'] <= 25:
            team_data['location'] = f"#{team_data['rank']} {team_data['location']}"
            
        return team_data

    def _get_odds_data(self, game, team1_data, team2_data):
        """Extract and process odds information."""
        odds_details = game['Column1.competitions.odds.details'].iloc[0]
        over_under = game['Column1.competitions.odds.overUnder'].iloc[0]
        
        if pd.isna(odds_details) or odds_details == "":
            return "ODDS UNAVAILABLE", "#fff", "#000"
        
        odds_text = f"{odds_details} O/U {over_under}"
        
        # Determine odds team colors
        odds_team = str(odds_details).split("-")[0].replace(" ", "")
        if odds_team == team1_data['abbreviation']:
            return odds_text, team1_data['color'], team1_data['alternate_color']
        elif odds_team == team2_data['abbreviation']:
            return odds_text, team2_data['color'], team2_data['alternate_color']
        else:
            return odds_text, "#fff", "#000"

    def _get_venue_data(self, game, team2_data):
        """Extract venue information and colors."""
        venue = f"At {game['Column1.competitions.venue.fullName'].iloc[0]}"
        
        if game['Column1.competitions.neutralSite'].iloc[0]:
            return venue, "#fff", "#000"
        else:
            return venue, team2_data['color'], team2_data['alternate_color']

    def _create_scoreboard_svg(self, game_data, dimensions):
        """Create and return base64 encoded SVG scoreboard."""
        scoreboard = generate_custom_scoreboard(
            team1_name=game_data['team1']['location'],
            team1_logo_url=game_data['team1']['logo'],
            team1_text_color=game_data['team1']['alternate_color'],
            team2_name=game_data['team2']['location'],
            team2_logo_url=game_data['team2']['logo'],
            team2_text_color=game_data['team2']['alternate_color'],
            venue=game_data['venue']['text'],
            venue_text_color=game_data['venue']['text_color'],
            score_line=game_data['odds']['text'],
            score_text_color=game_data['odds']['text_color'],
            team1_name_bg_color=game_data['team1']['color'],
            team1_logo_bg_color=game_data['team1']['color'],
            team2_name_bg_color=game_data['team2']['color'],
            team2_logo_bg_color=game_data['team2']['color'],
            venue_bg_color=game_data['venue']['bg_color'],
            score_bg_color=game_data['odds']['bg_color'],
            width=dimensions.get('width', 400) if dimensions else 400,
            height=dimensions.get('height', 60) if dimensions else 60
        )
        
        svg_string = scoreboard.as_svg()
        svg_base64 = base64.b64encode(svg_string.encode()).decode()
        
        return html.Img(
            src=f"data:image/svg+xml;base64,{svg_base64}",
            style={'width': '100%', 'height': 'auto', 'vertical-align': 'baseline'}
        )

    def _setup_callbacks(self):
        """Setup application callbacks."""
        @self.app.callback(
            [
                Output('schedule', 'groups'),
                Output('schedule', 'items'),
                Output('schedule', 'visibleTimeStart'),
                Output('schedule', 'visibleTimeEnd'),
                Output('schedule', 'minZoom'),
                Output('schedule', 'maxZoom'),
                Output('schedule', 'customGroupsContent'),
                Output('schedule', 'customItemsContent'),
                Output('schedule', 'itemsStyle'),
                Output('schedule', 'groupsStyle')
            ],
            [
                Input('schedule', 'itemClickData'),
                Input('schedule', 'itemDimensions'),
                Input('date-picker', 'date')
            ]
        )
        def update_schedule(click_data, dimensions, date_value):
            # Filter data by selected date
            df_filtered = self.df[self.df['Column1.competitions.date.1'] == date_value].copy()
            
            # Convert timestamps once
            df_filtered['start_time_ms'] = df_filtered['start_time'].astype("int64") // 10**6
            df_filtered['end_time_ms'] = df_filtered['end_time'].astype("int64") // 10**6
            
            # Calculate zoom range
            min_max_zoom = df_filtered['end_time_ms'].max() - df_filtered['start_time_ms'].min()
            
            # Initialize output lists
            groups, items = [], []
            custom_groups_content, custom_items_content = [], []
            
            # Process each unique station
            stations = df_filtered['Column1.competitions.broadcasts.names'].unique()
            
            for group_id, station in enumerate(stations):
                station_data = df_filtered[df_filtered['Column1.competitions.broadcasts.names'] == station]
                df_split = self._create_bins(station_data, 2)
                
                # Process each game in the station
                for game in df_split:
                    game = game.reset_index(drop=True)
                    
                    # Extract team data
                    team1_data = self._get_team_data(game, 1)
                    team2_data = self._get_team_data(game, 0)
                    
                    # Extract odds and venue data
                    odds_text, odds_bg, odds_text_color = self._get_odds_data(game, team1_data, team2_data)
                    venue_text, venue_bg, venue_text_color = self._get_venue_data(game, team2_data)
                    
                    # Create game data structure
                    game_data = {
                        'team1': team1_data,
                        'team2': team2_data,
                        'odds': {'text': odds_text, 'bg_color': odds_bg, 'text_color': odds_text_color},
                        'venue': {'text': venue_text, 'bg_color': venue_bg, 'text_color': venue_text_color}
                    }
                    
                    # Create timeline item
                    items.append({
                        'id': game['Column1.id'].iloc[0],
                        'group': group_id,
                        'title': f"{team1_data['location']} vs {team2_data['location']}\n{venue_text}\n{odds_text}",
                        'start_time': game['start_time_ms'].iloc[0],
                        'end_time': game['end_time_ms'].iloc[0],
                        'itemProps': {'style': {'background': 'transparent'}}
                    })
                    
                    # Create scoreboard content
                    custom_items_content.append(self._create_scoreboard_svg(game_data, dimensions))
                
                # Create group
                groups.append({
                    'id': group_id,
                    'title': station,
                    'stackItems': True
                })
                
                # Create group content (network logo)
                network_logo = station_data['Network Logo'].iloc[0]
                custom_groups_content.append(
                    html.Div([
                        html.Img(
                            src=network_logo,
                            style={"max-width": '100%', 'max-height': '100%'}
                        )
                    ], style={'width': '100%', 'height': '100%'}, className='text-center')
                )
            
            # Define styles
            custom_styles = {'height': '100%', 'width': '100%'}
            
            return [
                groups, items,
                df_filtered['start_time_ms'].min(),
                df_filtered['end_time_ms'].max(),
                min_max_zoom, min_max_zoom,
                custom_groups_content, custom_items_content,
                custom_styles, custom_styles
            ]

    def run(self, debug=True):
        """Run the application."""
        self.app.run(debug=debug)


# Create and run the application
if __name__ == '__main__':
    cfb_app = CFBGuideApp()
    cfb_app.run(debug=False)