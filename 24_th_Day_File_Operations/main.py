# Reading file
# with open('my_file.txt') as file:
#     contents = file.read()
#     print(contents)


# Writing to file
# with open('my_file.txt',mode='w') as file:
#     file.write("New line added")


# Append contents to a file
with open('my_file.txt',mode='a') as file:
    file.write("\nNew line added")