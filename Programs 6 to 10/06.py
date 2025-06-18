"""
02_01: Write a program to input a number nad print whther it is Even or Odd.    
"""
num = int(input("Enter any number: "))

if num % 2 == 0:
    print(f"{num} is a Even number.")
else:
    print(f"{num} is a Odd number.")