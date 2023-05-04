info_list = [
    ("Alan", 90),
    ("Bruce", 80),
    ("Carlos", 85),
    ("David", 92),
    ("Emma", 81),
]
dic = {}
for item in info_list:
    name = item[0]
    age = item[1]
    dic[name] = age
print(dic)