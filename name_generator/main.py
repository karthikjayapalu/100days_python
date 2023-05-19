import random
import itertools
from itertools import permutations

# names = ['Ed Sheeran', 'Beyonce', 'Adele', 'Rhianna']
names = ['Adaptable', 'Angst', 'Articulate', 'Audience', 'Authentic', 'Body language', 'Captivating', 'Charismatic',
         'Clarity', 'Clear', 'Coherence', 'Compelling', 'Confidence', 'Eloquent', 'Empathetic', 'Empowering',
         'Engaging', 'Enlightening', 'Enthusiastic', 'Exclaim', 'Express', 'Eye contact', 'Fear', 'Fluency', 'Humorous',
         'Imitate', 'Impactful', 'Impressive', 'Informative', 'Insightful', 'Inspirational', 'Intonation', 'Intuitive',
         'Language', 'Lean', 'Listening', 'Memorable', 'Motivational', 'Moving', 'Oral', 'Parrot', 'Passionate',
         'Persuasive', 'Podium', 'Point', 'Poised', 'Practice', 'Presentation', 'Professional', 'Profound',
         'Pronunciation', 'Publicspeaking', 'Reden', 'Relevant', 'Responsive', 'Saying', 'Speech', 'Stage', 'Statement',
         'Supportive', 'Tala', 'Thought-provoking', 'Tone', 'Understanding', 'Versatile', 'Vocabulary', 'Voice',
         'Well-delivered', 'Words']
random_names = random.sample(names, len(names))

# https://www.geeksforgeeks.org/program-find-initials-name/
# def printInitials(name):
#     if(len(name) == 0):
#         return
#     print(name[0].upper()),
#     for i in range(1, len(name) - 1):
#         if (name[i] == ' '):
#             print (name[i + 1].upper()),

# Get all the 1st letter from the list of words
initials_str = []

for n in names:
    initials_str.append(n[0])

initials_str = [*set(initials_str)]

print('List of 1st letters of the words from input --> ',initials_str,'--> len: ',len(initials_str))


# generate random 4 letter words with vowels in the 2nd position

import random

merged_initials = ''.join(initials_str) # Change your required characters here
print(merged_initials,'--> len: ',len(merged_initials))
n = 4 # Change your word length here

print(''.join(random.choices(merged_initials, k=5)))


def words(letters):
    for n in range(6, 7):
        yield from map(''.join, permutations(letters, n))
app_name=[]
for w in words(merged_initials):
    app_name.append(w)
    # print(w)
# print(app_name,'--> len:',len(app_name))

second_letter=['A','E','I','O','U']

new_app_names=[]
for na in app_name:
    # print(na[1])
    if na[1] in second_letter and na[2] in second_letter and na[5] in second_letter:
        new_app_names.append(na)

print(new_app_names,'--> len:',len(new_app_names))

with open('app_names.txt',mode='w') as file:

    for nam in new_app_names:
        file.write(nam+'\n')

print(type(words(merged_initials)))

import enchant
new_app_names_eng=[]

d = enchant.Dict("en_US")
for nam in new_app_names:
    if d.check(nam):
        new_app_names_eng.append(nam)



with open('app_name_en_words.txt',mode='w') as f:
    for n in new_app_names_eng:
        f.write(n+'\n')

print(new_app_names_eng,'--> len:',len(new_app_names_eng))
