'''
01_3: Write a program to input principal amount, rate of interest and number of years and
display the final simple interest.
'''
p = int(input("Enter Principal Amount: "))
r = float(input("Enter Rate of Ineterest: "))
n = int(input("Enter Number of Years: "))

i = (p * r * n)/ 100
print("Simple interest: ", i)
