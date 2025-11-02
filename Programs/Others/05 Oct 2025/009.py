"""
Additional 09: 
Write a program to calculate bill payment as per following condition:
take input of product id, product name, price and quantity and
calculate discount as per following condition:
-> if purchase amount is greater than 5000 then calculate discount 20% 
-> if purchase amount is between 3000 to 5000 then calculate discount 15% 
-> if purchase amount is between 1000 to 3000 then calculate discount 10% 
-> if purchase amount is below 1000 then calculate discount 5% 
and finally display product id, product name, price, quantity, discount and final_payment.
"""

print("*****Enter following requirnments to create bill*****")
product_id = input("Product Id: ")
product_name = input("Product Name: ")
price = float(input(f"Price of {product_name}: "))
quantity = int(input("Quantity: "))

purchase_amount = price * quantity

if purchase_amount >= 5000:
    discount = (purchase_amount * 20) / 100
    dis_per = 20
    
elif purchase_amount >= 3000 and purchase_amount < 5000:
    discount = (purchase_amount * 15) / 100
    dis_per = 15
    
elif purchase_amount >= 1000 and purchase_amount < 3000:
    discount = (purchase_amount * 10) / 100
    dis_per = 10
    
else:
    discount = (purchase_amount * 5) / 100
    dis_per = 5
final_payment = purchase_amount - discount

print("\n *****Final Bill****")
print(f"Produt Id: {product_id}")
print(f"Produt Name: {product_name}")
print(f"Price of {product_name}: {price}")
print(f"Quantity: {quantity}")
print(f"Discount {dis_per}%: {discount}")
print(f"Final payment: {final_payment}")
