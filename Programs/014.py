'''
Write a program to take 4 digit number from user and print sum of first and last digit.
Ex. 2368 = 2 + 8 = 10
'''

n = int(input("Enter number: "))

l = n % 10
f = n / 1000
print(f"Sum of {int(f)} and {l} is: {int(f) + l}")
