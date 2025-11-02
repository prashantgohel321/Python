'''
Write a program to take value in km from user and
convert km into cm, meter, feet and inch and print them.
'''

km = float(input("Enter Kilometer: "))

print(f"--- Km: {km} ---")
print(f"Km to Feet: {km * 3280.84}")
print(f"Km to Cm: {km * 100000}")
print(f"Km to Meter: {km * 3280.84}")
print(f"Km to Inch: {km * 39370.1}")
print(f"Km to Mile: {km * 0.62137}")
