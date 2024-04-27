from datetime import datetime

# Initialize variables
disc_rate = 0.10
sales_tax_rate = 0.06
subtotal = 0.0

print("Enter the price and quantity for your item(s).")
print()

# Loop to get items and prices
while True:
    price = float(input("Please enter item price(or '0' to finish): "))
    if price == 0:
        break
    quantity = int(input("Please enter the quantity: "))
    subtotal += price * quantity
    print()

# Output the subtotal
subtotal = round(subtotal, 2)
print(f"Subtotal: {subtotal:.2f}\n")

# Determine the current day
current_date = datetime.now()
weekday = current_date.weekday()

# Discount Code
if weekday == 1 or weekday == 2: 
    if subtotal >= 50:
        discount = round(subtotal * disc_rate, 2)
        print(f"Discount amount: {discount:.2f}")
        subtotal -= discount
    else:
        enough = 50 - subtotal
        print(f"To receive the discount, add {enough:.2f} to your order.")

# Calculate sales tax
sales_tax = round(subtotal * sales_tax_rate, 2)
print(f"Sales tax amount: {sales_tax:.2f}")

# Total calculation and display
total = subtotal + sales_tax
print(f"Total: {total:.2f}")
