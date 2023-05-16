lst = [8, 5, 7, 12, 19, 21, 10, 3, 2, 11]

arr = []
for i in range(len(lst)-1):
    d = lst[i+1] - lst[i]
    arr.append(d)
print(arr)




