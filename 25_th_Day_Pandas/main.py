# pandas documentation -- https://pandas.pydata.org/docs/
# pandas api reference -- https://pandas.pydata.org/docs/reference/index.html

import pandas as pd

data = pd.read_csv('weather_data.csv')

print(data)
print("\n**************\n")
def Average(lst):
    return sum(lst)/len(lst)

temp=data['temp'].to_list()

print(temp)
print("\n**************\n")
#CHALLENGE : Average of a column
# avg_temp=Average(temp)
avg_temp=data['temp'].mean()
print("Average:",round(avg_temp,2))
print("\n**************\n")
#CHALLENGE : Get the max of a column

max_temp=data['temp'].max()

print("MAXIMUM VALUE:",round(max_temp,2))
print("\n**************\n")
#Get the data in the Rows
print("Data from a particular row",data[data['day']=="Monday"])

#CHALLENGE: Print row of the data where the temp is at the maximum

print("Row of the data where temp is MAX",data[data['temp']==data['temp'].max()])
print("\n**************\n")
#CHALLENGE: Get monday's temp and convert it to farenheit

monday=data[data.day=="Monday"]
# print(monday)
mon_tem=int(monday.temp)
print(mon_tem)
mon_temp_f = (mon_tem*(9/5))+32
print("Monday's temp in farenheit:",mon_temp_f)
print("\n**************\n")

#create a dataframe from scratch

data_dict={
    "students":["Amy","James","Angela"],
    "scores":[76,56,65]
}

d=pd.DataFrame(data_dict)
print(d)
d.to_csv("new_data.csv")
print("\n**************\n")

