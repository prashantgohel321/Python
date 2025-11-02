"""
Number Triangle
1
1 2
1 2 3
1 2 3 4
"""

rows = 4
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(i, end = " ")
    print()