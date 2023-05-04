# 5-3
lst = ["range", "str", "continue", 12, True, "python", 3.14, "else"]
mi = 0
for i in range(len(lst)):
    if isinstance(lst[i],str):
        if len(lst[i]) > len(lst[mi]):
            mi = i
print(mi, lst[mi])




