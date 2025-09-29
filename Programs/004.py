'''
01_4: Write a program to input principal amount, rate and year and display compound interest.
'''
p = int(input("Enter Principal Amount: "))
r = float(input("Enter Rate of Ineterest: "))
n = int(input("Enter Number of Years: "))

a = p * pow((1 + (r / 100)), n)
print("Amount: ", a)
i = a - p
print("Compound interest: ", i)
