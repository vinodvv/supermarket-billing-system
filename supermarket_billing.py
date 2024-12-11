RUPEE_SYMBOL = "\u20B9"

def supermarket_billing():
    print("Welcome to the Supermarket Billing System!")

    # Get the number of items
    num_items = int(input("Enter the number of items: "))

    items = []

    for i in range(1, num_items + 1):
        print(f"\nItem {i}:")
        name = input("Name: ")
        price = float(input(f"Price per unit: {RUPEE_SYMBOL} "))
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
        print(f"{item['name']}: {RUPEE_SYMBOL}{item['price']} x {item['qty']} = {RUPEE_SYMBOL}{item_total}")

    # Apply discount if any (e.g., discount for subtotal above 50.0
    discount = 0
    if sub_total >= 50:
        discount = 0.1 * sub_total  # 10% discount

    # Calculate Sales Tax
    tax_rate = 0.05  # 5%
    tax = (sub_total - discount) * tax_rate

    # Calculate Total
    total = sub_total - discount + tax

    print(f"\nSub-Total: {RUPEE_SYMBOL}{sub_total:.2f}")
    print(f"Discount: {RUPEE_SYMBOL}{discount:.2f}")
    print(f"Sales Tax: {RUPEE_SYMBOL}{tax:.2f}")
    print(f"Total: {RUPEE_SYMBOL}{total:.2f}")
    print(f"\nThank you for shopping with us!")


# Run the programme
if __name__ == "__main__":
    supermarket_billing()
