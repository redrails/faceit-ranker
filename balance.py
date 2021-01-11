import json
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial.polynomial import polyfit


with open(r'./stats.json') as f:
    data = json.loads(f.read())


df = pd.json_normalize(data["players"])

del df['player_id']

df.set_index('nickname', inplace=True)
df = df.astype('float32')

pd.options.display.max_columns = df.shape[1]

'''

Features:
 - stats.Matches                 : Matches played in total
 - stats.Average Headshots %     : How good the aim is
 - stats.K/D Ratio               : How well you did in the game based on K/D ratio
 - stats.Win Rate %              : How many times you win
 - stats.Average Kills           : Participation average in games


 1. Get average number of games played by everyone - Scale = normalised distribution of matches played
 2. Take the number of matches played by a player and 

'''


match_values = df["stats.Matches"].value_counts()

x = np.array(match_values.index.tolist())
y = np.array(match_values)

plt.scatter(x, y)
# plt.show()


scaler = np.random.normal(match_values, scale = 1)
plt.plot(scaler)
plt.show()