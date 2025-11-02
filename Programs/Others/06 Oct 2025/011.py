'''
Write a program to print even number up to n length using while loop.
'''

n = int(input("Enter number: "))
i = 0

# Solution 01
# while i <= n:
#     print(i)
#     i += 1

# Solution 02
while i <= n:
    if i % 2 == 0:
        print(i)
    i += 1
