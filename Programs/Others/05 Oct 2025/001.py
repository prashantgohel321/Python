'''
Additional 01: 
Write a program to take 2 number inputs from user and interchange the values.
'''

# Solution 01: Using 2 variables only

print("\nBefore Swap\n")
f = int(input("First number: "))
s = int(input("Second number: "))

print("\nAfter Swap\n")
s -= f
f += s

print("First number: ", f)
s = f - s
print("Second number: ", s)




# Solution 02: Using 3rd variable
print("\nUsing 3rd variable\n")
temp = s
s = f
f = temp
print("First number: ", f)
print("Second number: ", s)




# Solution 03: Using 2 variables only (Pythonic way)
print("\nUsing Pythonic way\n")
f, s = s, f
print("First number: ", f)
print("Second number: ", s)