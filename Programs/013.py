'''
Write a program to take 2 number inputs from user and interchange the values.
'''

print("\nBefore Swap\n")
f = int(input("First number: "))
s = int(input("Second number: "))

print("\nAfter Swap\n")
s = s - f
f = f + s
print("First number: ", f)
s = f - s
print("Second number: ", s)
