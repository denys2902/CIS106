part = int(input("Enter part number: "))
quantity = int(input("Enter quantity: "))

if part == 10 or part == 55:
    price = 1.00
elif part == 99:
    price = 2.00
elif part == 80 or part == 70:
    price = 3.00
else:
    price = 5.00

total = quantity * price

print("Part number:", part)
print(f"Unit cost:  ${price:.2f}")
print(f"Total cost: ${total:.2f}")