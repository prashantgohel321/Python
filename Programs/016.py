'''
Write a python program in which input 5 subject marks and calculate total, percentage and result (Pass or Fail).
'''
print("*****Enter 5 subject marks*****")
s1 = float(input("Subject 1: "))
s2 = float(input("Subject 2: "))
s3 = float(input("Subject 3: "))
s4 = float(input("Subject 4: "))
s5 = float(input("Subject 5: "))

total = s1 + s2 + s3 + s4 + s5
percentage = total / 5

if s1 < 40 or s2 < 40 or s3 < 40 or s4 < 40 or s5 < 40:
    print("Result = Pass")
else:
    print("Result = Fail")
