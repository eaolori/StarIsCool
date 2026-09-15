price = float(input("Enter amount: "))
quantity = int(input("Enter quantity: "))
discount = float(input("Enter discount percent: "))

subtotal = price * quantity
discount_amount = subtotal * discount / 100
final_price = subtotal - discount_amount

print(f"Subtotal: {round(subtotal, 2)}")
print(f"Discount amount: {round(discount_amount, 2)}")
print(f"Final price: {round(final_price, 2)}")