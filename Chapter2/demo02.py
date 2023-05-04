names = "Alan, Bruce, Carlos, David, Emma"
name_list = names.split(",")
# print(name_list)
for name in name_list:
    name2 = name.strip()
    print('hello, %s'%name2)