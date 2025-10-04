''' 
Write a program to print all prime numbers between 1 to 100. 
''' 
print("*****Using for loop*****") 
for num in range(1, 100): 
    if num > 1: 
        for i in range(2, num): 
            if num % i == 0: 
                break 
        else: 
            print(num, end = ", ") 
 
 
 
print("\n\n*****Using while loop*****") 
i1 = 2 
while i1 < 100: 
    j = 2 
    while j < 100: 
        if i1 % j == 0: 
            break 
        j += 1 
    if i1 == j: 
        print(i1, end = ", ") 
    i1 += 1 