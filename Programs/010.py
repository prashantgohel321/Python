"""
02_05: Write a program to print all numbers which are divisible by 7 in between 1 to 200.    
"""
print("*****Here the numbers are divisible by 7 between 1 to 200.*****")
for i in range(1, 201):
    if i % 7 == 0:
        print(i, end = ", ")