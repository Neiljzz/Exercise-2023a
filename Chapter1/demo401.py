"""
i   part2
0   1
1   3
2   5
3   7
"""

for i in range(5):
    part1 = " " * (4-i)
    part2 = "A" * (i * 2 + 1)
    print(part1 + part2)