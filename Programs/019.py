"""
Write a program which takes input of 2 numbers and operator, and display result as per input operator.    
"""

num1 = int(input("Enter any number: "))
num2 = int(input("Enter any number: "))

op = input("Enter an Operator: ")

if op == "+":
    print(f"{num1} {op} {num2} = {num1 + num2} (Addition)")
elif op == "-":
    print(f"{num1} {op} {num2} = {num1 - num2} (Subtraction)")
elif op == "*":
    print(f"{num1} {op} {num2} = {num1 * num2} (Multiplication)")
elif op == "/":
    print(f"{num1} {op} {num2} = {num1 / num2} (Division)")
elif op == "%":
    print(f"{num1} {op} {num2} = {num1 % num2} (Modulo)")
else:
    print(f"{op} is an invalid operator.")
