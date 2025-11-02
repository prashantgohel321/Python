"""
Inverted Pyramid
* * * * * 
 * * * * 
  * * * 
   * * 
    *
"""

rows = 5
for i in range(rows, 0, -1):
    print(" " * (rows - i) + "* " * i)