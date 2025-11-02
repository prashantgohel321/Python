"""
Pascal’s Triangle
      1
     1 1
    1 2 1
   1 3 3 1
  1 4 6 4 1
"""

from math import comb
rows = 5
for i in range(rows):
    print(" " * (rows - i), end="")
    for j in range(i + 1):
        print(comb(i, j), end=" ")
    print()