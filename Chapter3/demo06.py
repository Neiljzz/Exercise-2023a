# 5-2
lst = [8, 5, 7, 12, 19, 21, 10, 3, 2, 11]
mi = 0
for i in range(len(lst)):
    if lst[i] < lst[mi]:
        mi = i
print(lst[mi], mi)