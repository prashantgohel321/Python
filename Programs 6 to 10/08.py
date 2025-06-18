"""
02_03: Write a python program to input marks of 4 subject and display Total, Percentage, Result and Grade.    
       If student is fail (<40) in any subject then result should be displayed as fail and with held** and otherwise display result as pass
"""
print("****Enter 4 subject marks****")
s1 = float(input("Subject 1: "))
s2 = float(input("Subject 2: "))
s3 = float(input("Subject 3: "))
s4 = float(input("Subject 4: "))

total = s1 + s2 + s3 + s4
print(f"Total: {total}")
percentage = total / 4
print(f"Percentage: {percentage}")

# Result
if s1 < 40 or s2 < 40 or s3 < 40 or s4 < 40:
    print("Result: FAIL")
    print("With Held**")
else:
    print("Result PASS")
    # Grade
    if total >= 380:
        print("Grade = O")
    elif total >= 320 and total < 380:
        print("Grade = A")
    elif total >= 280 and total < 320:
        print("Grade = B")
    elif total >= 220 and total < 280:
        print("Grade = C")
    else:
        print("Grade = D")