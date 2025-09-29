"""
-> 02_02: Write a program to input age of person and display message as follows:
       if age less than 12 then display: You are a Kid.
       if age is between 12 to 17 then display: You are a Teenager.
       if age is between 18 to 60` then display: You are a Adult.
       if age greater than 60 then display: You are a Senior citizen..
"""
age = int(input("Enter your age: "))
if age < 12:
    print("You are a Kid.")
    
elif age >= 12 and age <= 17:
    print("You are a Teenager.")
    
elif age >= 18 and age <= 60:
    print("You are a Adult.")
    
else:
    print("You are a Senior citizen.")