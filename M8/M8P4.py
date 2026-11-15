total_extended = 0.0
count = 0
with open("items.txt", "r") as file:
    while True:
        item = file.readline().strip()
        if not item:
            break
        quantity = int(file.readline().strip())
        price = float(file.readline().strip())
        extended = quantity * price
        total_extended += extended
        count += 1
        print(f"{item}: Quantity {quantity}, Price ${price:,.2f}, Extended ${extended:,.2f}")
print(f"Sum of extended prices: ${total_extended:,.2f}")
print(f"Number of orders: {count}")
if count:
    print(f"Average order: ${total_extended / count:,.2f}")
