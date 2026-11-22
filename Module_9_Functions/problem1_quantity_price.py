def extended_price(quantity, price):
    total = quantity * price
    if total > 10000:
        total = total * 0.90
    return total


total_extended_price = 0
while True:
    entry = input("Enter quantity (or stop): ")
    if entry.lower() == "stop":
        break
    quantity = int(entry)
    price = float(input("Enter unit price: "))
    total = extended_price(quantity, price)
    print(f"Quantity: {quantity}, Price: ${price:.2f}, Extended price: ${total:.2f}")
    total_extended_price += total

print(f"Total extended price: ${total_extended_price:.2f}")
