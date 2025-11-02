'''
Write a program to print multiplication table of given number using while and for loop.
'''

n = int(input("Enter number: "))
i = 1

# Using While Loop
print("\n--- Using While Loop --- \n")
while i <= 10:
    print(f"{n} X {i} = {n * i}")
    i += 1


print("\n--- Using For Loop --- \n")
for i in range(11):
    print(f"{n} X {i} = {n * i}")
    