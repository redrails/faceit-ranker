import json
import pandas as pd

data = None

with open('./data.json') as f:
  data = json.loads(f.read())

df = pd.json_normalize(data)

df.set_index('nickname', inplace=True)
pd.options.display.max_columns = df.shape[1]


del df['player_id']
df = df.astype('float32')

def isgood(player, stat):
  selected_player = df.loc[player]
  selected_player_stat = selected_player[stat]
  if(selected_player_stat < df[stat].mean()):
    return "you are shite"
  else:
    return "you are average"

df.sort_values('stats.Average Kills', inplace=True, ascending=False)

#print(df)

# print(df.describe(include='all'))
print(df['stats.Average Kills'])
# print(isgood('G_Dez', 'stats.Average Deaths'))
# print(isgood('redrails', 'stats.Average Deaths'))
