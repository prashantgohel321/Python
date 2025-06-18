"""
02_04: Write a program to input a number and display table of that number.    
"""
num = int(input("Enter any number: "))
for i in range(1, 11):
    print(f"{num} X {i} = {num * i}")