def get_max(lst):
    m = lst[0]
    for item in lst:
        if item > m:
            m = item
    return m

def get_min(lst):
    mv = lst[0]
    # for i in range(len(lst)):
    #     if lst[i] < mv:
    #         mv = lst[i]
    # return mv

    for item in lst:
        if item < mv:
            mv = item
    return mv

def cal_max_diff(lst):
    max_v = get_max(lst)
    min_v = get_min(lst)
    max_diff = max_v - min_v
    return max_diff

arr1 = [13, 15, 12, 19, 5, 7, 10]
r = cal_max_diff(arr1) # 19 - 5 = 14
print(r)

arr2 = [15, 35, 122, 149, 1235, 437, 110]
r = cal_max_diff(arr2)
print(r)