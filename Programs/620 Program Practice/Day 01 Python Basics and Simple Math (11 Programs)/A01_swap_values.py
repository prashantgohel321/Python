"""
Swap the values of two variables (using temporary variable AND Python tuple unpacking).
"""

try:
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
except ValueError:
    print("\n ***** Please enter valid numeric values. ***** \n")
    exit()

# using temporary variable
print("\n--- Before Swapping ---")
print(f"a = {a}, b = {b}")
temp = a
a = b
b = temp

print("\n--- After Swapping ---")
print("Using Temporary Variable")
print(f"a = {a}, b = {b}")

# pythonic way; tuple unpacking
print("\nUsing Tuple Unpacking")
a, b = b, a
print(f"a = {a}, b = {b}\n")
