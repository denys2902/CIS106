# Module 3 - Problem 4: Car discount
make = input("Enter car make: ")
model = input("Enter car model: ")
msrp = float(input("Enter MSRP: "))
discount = float(input("Enter discount as a decimal (example 0.10): "))

amount_off = msrp * discount
discounted_price = msrp - amount_off

print("Make:", make)
print("Model:", model)
print(f"MSRP: ${msrp:.2f}")
print(f"Discount percent: {discount * 100:.2f}%")
print(f"Amount off: ${amount_off:.2f}")
print(f"Discounted price: ${discounted_price:.2f}")
