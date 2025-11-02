"""
Hollow Pyramid
    *
   * *
  *   *
 *     *
* * * * *
"""

rows = 5
for i in range(1, rows + 1):
    for j in range(1, rows + 1):
        if j == rows - i + 1 or j == rows + i - 1 or i == rows:
            print("*", end="")
        else:
            print(" ", end="")
    print()