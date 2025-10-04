''' 
Write a program to input a number and display whether number is prime 
or not. 
''' 

num = int(input("Enter number: ")) 
flag = 0 
 
print("\n\n*****Using for loop*****") 
for i in range(2, num): 
    if num % i == 0: 
        flag += 1 
        break 
 
if flag == 1: 
    print(f"{num} is not a Prime number.") 
else: 
    print(f"{num} is Prime number.") 
 
 
 
print("\n\n*****Using while loop*****") 
i1 = 2 
flag1 = 0 
while i1 < num: 
    if num % i1 == 0: 
        flag1 += 1 
        break 
    i1 += 1 
 
if flag1 == 1: 
    print(f"{num} is not a Prime number.") 
else: 
    print(f"{num} is Prime number.") 