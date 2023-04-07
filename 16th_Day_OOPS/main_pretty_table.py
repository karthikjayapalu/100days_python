from prettytable import PrettyTable

x = PrettyTable()

d = {
    "Pikachu": "Electric",
    "Squirtle": "Water",
    "Charmander": "Fire"
}

x.field_names = ["Pokemon Name", "Type"]
# x.add_row(["Pikachu", "Electric"])
# x.add_row(["Squirtle", "Water"])
# x.add_row(["Charmander", "Fire"])
for k, v in d.items():
    x.add_row([k, v])
x.align = 'l'
print(x)
