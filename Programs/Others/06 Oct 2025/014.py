'''
Right-Angled Triangle
*
* * 
* * *
* * * *
* * * * *
'''

# Solution 01
for i in range(6):
    for j in range(i + 1):
        print("*", end = " ")
    print()

# Solution 02
rows = 5
for i in range(1, rows + 1):
    print("* " * i)