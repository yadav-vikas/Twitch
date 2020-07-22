import codecademylib3_seaborn
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

# Bar Graph: Featured Games

games = ["LoL", "Dota 2", "CS:GO", "DayZ", "HOS", "Isaac", "Shows", "Hearth", "WoT", "Agar.io"]

viewers =  [1070, 472, 302, 239, 210, 171, 170, 90, 86, 71]

fig,ax=plt.subplots(figsize=(12,10))
plt.bar(range(len(games)),viewers,color='blue')
ax.set_xticks([0,1,2,3,4,5,6,7,8,9])
ax.set_xticklabels(games)
plt.xlabel('viewers')
plt.ylabel('game')
plt.legend(["Twitch"])
plt.title('game vs viewers')
plt.clf()
# Pie Chart: League of Legends Viewers' Whereabouts

labels = ["US", "DE", "CA", "N/A", "GB", "TR", "BR", "DK", "PL", "BE", "NL", "Others"]

countries = [447, 66, 64, 49, 45, 28, 25, 20, 19, 17, 17, 279]

colors = ['lightskyblue', 'gold', 'lightcoral', 'gainsboro', 'royalblue', 'lightpink', 'darkseagreen', 'sienna', 'khaki', 'gold', 'violet', 'yellowgreen']

explode = (0.1, 0.1, 0.2, 0.1, 0.01, 0.02, 0, 0, 0, 0, 0, 0)

plt.pie(countries, explode=explode, colors=colors, shadow=True, startangle=345, autopct='%1.0f%%', pctdistance=1.15)
plt.title("LOL Whereabouts")
plt.legend(labels)
plt.clf()

# Line Graph: Time Series Analysis

hour = range(24)

viewers_hour = [30, 17, 34, 29, 19, 14, 3, 2, 4, 9, 5, 48, 62, 58, 40, 51, 69, 55, 76, 81, 102, 120, 71, 63]


y_upper=[i+i*0.15 for i in viewers_hour]
y_lower=[i-i*0.15 for i in viewers_hour]
fig,ax=plt.subplots(figsize=(12,10))
ax.set_xticks(range(24))
plt.plot(hour,viewers_hour)
plt.fill_between(hour,y_upper,y_lower,alpha=0.2)
plt.title('Time Series')
plt.xlabel('Viewers')
plt.ylabel('Hour')
plt.legend(['2015-01-01'])

plt.show()
