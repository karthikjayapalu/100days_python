# dataset - https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw
import pandas as pd

data=pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

#CHALLENGE : create count of squirrel colors in a separate csv file

color=data['Primary Fur Color']
print(color.value_counts())
color.value_counts().to_csv('squirrel_count.csv')