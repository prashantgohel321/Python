'''
Write a program to take value in km from user and
convert km into cm, meter, feet and inch and print them.
'''

km = float(input("Enter Kilometer: "))

feet = km * 3281
cm = km * 100000
m = km * 1000
inch = km * 39370

print(f"{km} (KM) = {feet} Feet")
print(f"{km} (KM) = {cm} CM")
print(f"{km} (KM) = {m} Meter")
print(f"{km} (KM) = {inch} Inch")
