"""
Calculate the sum of the first and last digit of a 4-digit integer.
2058 = 2+8 = 10
"""

num = 3058

try: 
    num = int(input("Enter 4 digit number: "))
    
    if num < 1000 or num > 9999:
        raise ValueError("Not a 4 digit number")
except ValueError as e:
    print(f"\n ***** {e} ***** \n")
    exit()

last_digit = num % 10 # 3058 % 10 = 8
first_digit = num // 1000 # 3058 / 1000 = 3.058; because of // it will be 3

sum = first_digit + last_digit
print(f"\n ***** Sum of first and last digit of {num} is {sum} ***** \n")