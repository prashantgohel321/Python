"""
Convert distance in Kilometers (km) to Centimeters (cm), Meters (m), Feet (ft), and Inches (in).
"""
try:
    km = float(input("Enter distance in Kilometers (km): "))
except ValueError:
    print("****** Please enter valid numeric value in km ******")
    exit()
    
cm = km * 100000          # 1 km = 100000 cm
m = km * 1000             # 1 km = 1000 m
ft = km * 3280.84        # 1 km = 3280.84 ft
inches = km * 39370.1    # 1 km = 39370.1 inches