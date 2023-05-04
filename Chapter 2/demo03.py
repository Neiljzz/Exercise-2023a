infos = [
    "Alan, 19",
    "Bruce, 22",
    "Carlos, 23",
    "David, 18",
    "Emma, 21"
]

for item in infos:
    new_item = item.split(",")
    age = new_item[1].strip()
    print("I am %s. I'm %s years old" %(new_item[0], age))
    


