total_discount = 0.0
answer = input("Do you want to continue? Yes/No: ")
while answer.strip().lower() == "yes":
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter item price: "))
    extended_price = quantity * price
    if extended_price > 10000:
        discount_percent = 0.25
    else:
        discount_percent = 0.10
    discount_amount = extended_price * discount_percent
    total = extended_price - discount_amount
    total_discount += discount_amount
    print(f"Extended Price: ${extended_price:.2f}")
    print(f"Discount Amount: ${discount_amount:.2f}")
    print(f"Total: ${total:.2f}")
    answer = input("Do you want to continue? Yes/No: ")
print(f"Sum of All Discounts: ${total_discount:.2f}")
