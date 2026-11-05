quantity = int(input("Enter number of tickets: "))

if quantity >= 25:
    price = 50.00
elif quantity >= 10:
    price = 60.00
elif quantity >= 5:
    price = 70.00
else:
    price = 75.00

total = quantity * price

print("Tickets:", quantity)
print(f"Price per ticket: ${price:.2f}")
print(f"Total cost:       ${total:.2f}")