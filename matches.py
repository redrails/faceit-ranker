import json
import pandas as pd
from tabulate import tabulate

# LOAD DATA, NEEDS TO BE AN API CALL IN FUTURE
with open('./match.json') as f:
  data = json.loads(f.read())

# Player data from game
team_1_player_data = data["rounds"][0]["teams"][0]["players"]
team_2_player_data = data["rounds"][0]["teams"][1]["players"]

# Team scores from game e.g. W/L and rounds W/L
team_1_score_data = data["rounds"][0]["teams"][0]["team_stats"]
team_2_score_data = data["rounds"][0]["teams"][1]["team_stats"]

# GET THE PLAYER DATA AS FLATTENED TABLE IN DATAFRAME
team1playersdf = pd.json_normalize(team_1_player_data)
team2playersdf = pd.json_normalize(team_2_player_data)

# GET THE TEAM STATS DATA AS FLATTENED TABLE IN DATAFRAME
team1statsdf = pd.json_normalize(team_1_score_data)
team2statsdf = pd.json_normalize(team_2_score_data)

# Set index of tables to player nicknames to easily interpret who's who
team1playersdf.set_index('nickname', inplace=True)
team2playersdf.set_index('nickname', inplace=True)

# No need for player ids
del team1playersdf["player_id"]
del team2playersdf["player_id"]

# Set data types to floats so that we can calculate stuff on them
team1playersdf = team1playersdf.astype('float32')
team2playersdf = team2playersdf.astype('float32')

# NOT SURE WHAT THE FUCK IS HAPPENING HERE
pd.options.display.max_columns = team1playersdf.shape[1]
pd.options.display.max_columns = team2playersdf.shape[1]


print(tabulate(team2playersdf.describe(include='all'), headers='keys', tablefmt='psql'))



# print(df)

# del df['player_id']
# df = df.astype('float32')

# def isgood(player, stat):
#   selected_player = df.loc[player]
#   selected_player_stat = selected_player[stat]
#   if(selected_player_stat < df[stat].mean()):
#     return "you are shite"
#   else: 
#     return "you are average"

# df.sort_values('stats.Average Kills', inplace=True, ascending=False)
# # print(df.describe(include='all'))
# print(df['stats.Average Kills'])
# # print(isgood('G_Dez', 'stats.Average Deaths'))
# # print(isgood('redrails', 'stats.Average Deaths'))
