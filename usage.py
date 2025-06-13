import pandas as pd
import numpy as np
import dash
from dash import html,dcc,Input,Output,State
import dash_bootstrap_components as dbc
from datetime import datetime, time
import os
from dash_calendar_timeline import DashCalendarTimeline
from usage_banner import generate_custom_scoreboard
import base64


app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP],
meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1.0"}
    ]
    )

server = app.server

data = os.path.join(os.path.dirname(os.path.abspath(__file__)),'./Fiverr Example Data v5.xlsx')
df = pd.read_excel(data)

df['start_time'] = pd.to_datetime(df['Column1.competitions.date.1'].astype(str) +" "+ df['Column1.competitions.date.2'].astype(str))


df['end_time'] = pd.to_datetime(df['start_time'].astype(str)) + pd.DateOffset(hours=3, minutes=30)

min_date = df['Column1.competitions.date.1'].min()
max_date = df['Column1.competitions.date.1'].max()


def create_bins(df,n):
    x = round(len(df)/n)
    res = np.array_split(df, x)
    return res


app.layout = dbc.Container(
      [
            dbc.NavbarSimple(
                  brand="CFB Guide",
                  brand_href="#",
                  color="danger",
                  dark=True
            ),
            dbc.Container(
                  [
                        dcc.DatePickerSingle(
                            id='date-picker',
                            min_date_allowed=datetime(min_date.year,min_date.month,min_date.day),
                            max_date_allowed=datetime(max_date.year,max_date.month,max_date.day),
                            initial_visible_month=datetime(min_date.year,min_date.month,min_date.day),
                            date=datetime(min_date.year,min_date.month,min_date.day),
                            style={'zIndex':100}
                        ),
                        DashCalendarTimeline(
                            id='schedule',
                            defaultTimeStart=(df['start_time'].astype('int64') / 10**6).min(),
                            defaultTimeEnd=(df['start_time'].astype('int64') / 10**6).min() + 24 * 60 * 60 * 1000,
                            sidebarWidth=100,
                            lineHeight=60,
                            itemHeightRatio=1,
                        #     dragSnap=15 * 60 * 1000,
                            maxZoom=24 * 60 * 60 * 1000,
                        #     minZoom=24 * 60 * 60 * 1000,
                            canMove=True,
                            canResize='both',
                            canChangeGroup=True,
                            sidebarHeaderVariant='left',
                            sidebarHeaderContent=html.H3("Station",className='text-center'),
                        #     timelineHeaderStyle={'background-color':'green'},
                        #     dateHeaderUnit='hour',
                        #     dateHeaderLabelFormat='HH:mm',
                            # groupTitleStyle={'font-size':'20px','font-weight':'bold'},
                            customGroups=True,
                            customItems=True,
                            dragInfoLabel=True,
                            traditionalZoom=False,
                            selectedItemColor='rgba(50, 245, 39, 0.5)',
                            showTodayMarker=True,
                            todayMarkerInterval=2000,
                            todayMarkerStyle={'background-color':'green'},
                            customMarkers=[
                                 {'date': 1750070400000, 'style': {'background-color': 'red'}},
                                 {'date': 1750675200000, 'style': {'background-color': 'blue'}}
                            ],
                            showCursorMarker=True,
                            cursorMarkerStyle={'background-color': 'red'}
                        #     draggingItemColor="purple",
                        #     resizingItemBorder="2px solid black"
                        ),
                        # html.Button("Save",id='save-items',n_clicks=0)

                  ],className='pt-5'
            )
            
            
            

      ],fluid=True,className='p-0'
)

# @app.callback(
#       Output('save-items','children'),
#       Input('save-items','n_clicks'),
#       State('schedule','items')
# )
# def update_items(n,items):
#      print(items)
#      return "Saved"

@app.callback(
      [Output('schedule','groups'),
      Output('schedule','items'),
      Output('schedule','visibleTimeStart'),
      Output('schedule','visibleTimeEnd'),
      Output('schedule','customGroupsContent'),
      Output('schedule','customItemsContent'),
      Output('schedule','itemsStyle'),
      Output('schedule','groupsStyle')],
      [Input('schedule','itemClickData'),
      Input('date-picker','date')]
)
def update_schedule(click_data,date_value):
    print(click_data)
    df_filtered_by_date = df[df['Column1.competitions.date.1'] == date_value]
    df_filtered_by_date['start_time'] = df_filtered_by_date['start_time'].astype("int64") // 10**6
    df_filtered_by_date['end_time'] = df_filtered_by_date['end_time'].astype("int64") // 10**6
  
    groups = []
    customGroupsContent = []
    items = []
    customItemsContent = []
  
    for group_id,station in enumerate(df_filtered_by_date['Column1.competitions.broadcasts.names'].unique()):

        df_filtered = df_filtered_by_date[df_filtered_by_date['Column1.competitions.broadcasts.names'] == station]
        df_split = create_bins(df_filtered,2)
    
        for game in df_split:
    
            game.reset_index(drop=True,inplace=True)
            team1_logo = game['Column1.competitions.competitors.team.logo'][1]
            
            team1_bg_color = '#'+game['Column1.competitions.competitors.team.color'][1]
            team1_location = game['Column1.competitions.competitors.team.location'][1]
            team1_text_color = '#'+game['Column1.competitions.competitors.team.alternateColor'][1]
            team2_logo = game['Column1.competitions.competitors.team.logo'][0]
            team2_bg_color = '#'+game['Column1.competitions.competitors.team.color'][0]
            team2_location = game['Column1.competitions.competitors.team.location'][0]
            team2_text_color = '#'+game['Column1.competitions.competitors.team.alternateColor'][0]
            venue = 'At '+game['Column1.competitions.venue.fullName'][0]
            odds_details = str(game['Column1.competitions.odds.details'][0]) + " O/U " + str(game['Column1.competitions.odds.overUnder'][0])
            network_logo = game['Network Logo'][0]
            team1_abbr = game['Column1.competitions.competitors.team.abbreviation'][1]
            team2_abbr = game['Column1.competitions.competitors.team.abbreviation'][0]
                        
      
            if game['Column1.competitions.odds.details'][0] != "":
                  
                  if str(game['Column1.competitions.odds.details'][0]).split("-")[0].replace(" ","") == team1_abbr:
                        odds_background = team1_bg_color
                        odds_text_color = team1_text_color
                  elif str(game['Column1.competitions.odds.details'][0]).split("-")[0].replace(" ","") == team2_abbr:
                        odds_background = team2_bg_color
                        odds_text_color = team2_text_color
                  else:
                        odds_background = "#fff"
                        odds_text_color = "#000"
                        odds_details = "ODDS UNAVAILABLE"
            if game['Column1.competitions.neutralSite'][0] == False:
                  venue_bg_color = team2_bg_color
                  venue_text_color = team2_text_color
            else:
                  venue_bg_color = "#fff"
                  venue_text_color = "#000"
      
            if game['Column1.competitions.competitors.curatedRank.current'][0] <= 25:
                  team2_location = '#'+str(game['Column1.competitions.competitors.curatedRank.current'][0]) + ' ' + team2_location
            if game['Column1.competitions.competitors.curatedRank.current'][1] <= 25:
                  team1_location = '#'+str(game['Column1.competitions.competitors.curatedRank.current'][1]) + ' ' + team1_location
      
      
            items.append({
              'id': game['Column1.id'][0],
              'group': group_id,
              'title': str(team1_location+" vs "+team2_location + "\u000d" + venue + "\u000d" + odds_details),
              'start_time': game['start_time'][0],
              'end_time': game['end_time'][0],
              'itemProps':{
                  'style':{
                        'background':'transparent',
                        # 'borderRadius':'5px',
                        'border': '2px solid #000',
                  }
              }
            })

            scoreboard = generate_custom_scoreboard(
                team1_name=team1_location,
                team1_logo_url=team1_logo,
                team1_text_color=team1_text_color,
                team2_name=team2_location, 
                team2_logo_url=team2_logo,
                team2_text_color=team2_text_color,
                venue=venue,
                venue_text_color=venue_text_color,
                score_line=odds_details,
                score_text_color=odds_text_color,
                team1_name_bg_color=team1_bg_color,
                team1_logo_bg_color=team1_bg_color,
                team2_name_bg_color=team2_bg_color,
                team2_logo_bg_color=team2_bg_color,
                venue_bg_color=venue_bg_color,
                score_bg_color=odds_background
                
            )

            svg_string = scoreboard.as_svg()
            svg_base64 = base64.b64encode(svg_string.encode()).decode()
            
            banner_content = html.Img(
                src="data:image/svg+xml;base64,{}".format(svg_base64),
                style={'max-width': '100%', 'max-height': '100%','vertical-align':'baseline'}
            )

            customItemsContent.append(banner_content)

            # customItemsContent.append(dbc.Row(
            #       [
            #             dbc.Col(
            #                   [
            #                            html.Img(src=team1_logo,style={'background-color':team1_bg_color,'max-width':'100%','max-height':'100%','vertical-align':'baseline'})

            #                   ],width=4,className='text-center',style={'height':'100%','width':'auto'}
            #             ),
            #             dbc.Col(
            #                   [
            #                        "VS"
            #                         # html.Div(team1_location,style={'background-color':team1_bg_color,'color':team1_text_color,'float':'left'}),
            #                         # html.Div("vs "+team2_location,style={'background-color':team2_bg_color,'color':team2_text_color,'float':'left'}),
            #                         # html.Div(venue,style={'background-color':venue_bg_color,'color':venue_text_color}),
            #                         # html.Div(odds_details,style={'background-color':odds_background,'color':odds_text_color})

            #                   ],width=4,style={'color':'#000','height':'100%','width':'auto'}
            #             ),
            #             dbc.Col(
            #                   [
            #                           html.Img(src=team2_logo,style={'background-color':team2_bg_color,'max-width':'100%','max-height':'100%','vertical-align':'baseline'})

            #                   ],width=4,className='text-center',style={'height':'100%','width':'auto'}
            #             )
            #       ],className='g-0',style={'width':'100%','height':'100%'},justify='between'
            # ))
        groups.append({
          'id': group_id,
          'title': station,
          'stackItems': True
        })

        customGroupsContent.append(
            html.Div(
                  [
                        html.Img(src=network_logo,style={"max-width":'100%','max-height':'100%'})
                  ],style={'width':'100%','height':'100%'},className='text-center'
            )
        )
    customItemsStyle={'height':'100%','width':'100%'}
    customGroupsStyle={'height':'100%','width':'100%'}
    return [groups,items,
            df_filtered_by_date['start_time'].min(),
            df_filtered_by_date['end_time'].max(),
            customGroupsContent,
            customItemsContent,
            customItemsStyle,
            customGroupsStyle]
    
    



if __name__ == '__main__':
    app.run(debug=True)