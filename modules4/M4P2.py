
# Module 4 - Problem 2
purchase_price = float(input("Enter purchase price per share: "))
current_price = float(input("Enter current stock price: "))
quantity = int(input("Enter number of shares: "))

value = (current_price - purchase_price) * quantity

print(f"Increase or decrease in value: ${value:.2f}")
