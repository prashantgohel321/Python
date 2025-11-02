"""
Additional 07: 
Write a program which takes input of 2 numbers and operator, and display result as per input operator.    
"""

import sys

num1 = int(input("Enter any number: "))
num2 = int(input("Enter any number: "))

op = input("Enter an Operator: ")

if op == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
elif op == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
elif op == "*":
    print(f"{num1} * {num2} = {num1 * num2}")
elif op == "/":
    if num2 == 0:
        print("Number should not be zero. It leads to ZeroDivisionError.")
        sys.exit()
    else:
        print(f"{num1} / {num2} = {num1 / num2}")
elif op == "%":
    if num2 == 0:
        print("Number should not be zero. It leads to ZeroDivisionError.")
        sys.exit()
    else:
        print(f"{num1} % {num2} = {num1 % num2}")
    

# Solution 2: Using Match Case
"""Python 3.10 introduced the match-case statement, which provides a more structured and powerful way to handle pattern matching, similar to a switch-case."""
match op:
    case "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    case "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    case "*":
        print(f"{num1} * {num2} = {num1 * num2}")
    case "/":
        if num2 == 0:
            print("Number should not be zero. It leads to ZeroDivisionError.")
            sys.exit()
        else:
            print(f"{num1} / {num2} = {num1 / num2}")
    case "%":
        if num2 == 0:
            print("Number should not be zero. It leads to ZeroDivisionError.")
            sys.exit()
        else:
            print(f"{num1} % {num2} = {num1 % num2}")