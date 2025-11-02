"""
Additional 08: 
Write a program which takes input of income and gender, and display message whether income is taxable or not as per following condition:

if gender = male and income is greater than 700000 and if gender = female and income is greater than 500000
display message taxable.
"""

income = int(input("Enter your income: "))
gender = input("Enter your gender. Type 'M' for Male and Type 'F' for female: ").lower()

if gender == "m":
    if income >= 700000:
        print("Taxable")
    else:
        print("Non-Taxable")
else:
    if income >= 500000:
        print("Taxable")
    else:
        print("Non-Taxable")