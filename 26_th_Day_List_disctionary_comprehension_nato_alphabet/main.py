#list

l1 = [int(line.rstrip()) for line in open('file1.txt')]
l2 = [int(line.rstrip()) for line in open('file2.txt')]
result=[n for n in l1 if n in l2]
print(result)


#dictionary 1

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

result = {word:len(word) for word in sentence.split()}
print(result)

#dictionary 1
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


#First *fork* your copy. Then copy-paste your code below this line 👇
#Finally click "Run" to execute the tests

#temp_f=(temp_c*9/5)+32

weather_f={day:(temp_c*9/5)+32 for(day,temp_c) in weather_c.items()}

print(weather_f)