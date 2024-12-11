print("Welcome to the Supermarket Billing System!")

# Get the number of items
num_items = int(input("Enter the number of items: "))

items = []

for i in range(1, num_items + 1):
    print(f"\nItem {i}:")
    name = input("Name: ")
    price = float(input("Price per unit: "))
    qty = float(input("Quantity: "))

    items.append({
        "name": name,
        "price": price,
        "qty": qty
    })

# Bill summary calculations
print("\n--- Bill Summary ---")

sub_total = 0

for item in items:
    item_total = item['price'] * item['qty']
    sub_total += item_total
    print(f"{item['name']}: {item['price']} x {item['qty']} = {item_total}")

# Apply discount if any (e.g., discount for subtotal above 50.0
discount = 0
if sub_total >= 50:
    discount = 0.1 * sub_total  # 10% discount

# Calculate Sales Tax
tax_rate = 0.05  # 5%
tax = (sub_total - discount) * tax_rate

# Calculate Total
total = sub_total - discount + tax

print(f"\nSub-Total: {sub_total:.2f}")
print(f"Discount: {discount:.2f}")
print(f"Sales Tax: {tax:.2f}")
print(f"Total: {total:.2f}")
print(f"\nThank you for shopping with us!")
