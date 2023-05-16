"""
i
0   +
1   -
2   +
3   -
"""

s = 0
for i in range(1000):
    k = (-1)**i
    v = 1/(i+1) * k
    s += v
print(s)