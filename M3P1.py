# Module 3 - Problem 1: Stock investment
symbol = input("Enter stock symbol: ")
shares = int(input("Enter number of shares: "))
price = float(input("Enter cost per share: "))

investment = shares * price

print("Stock:", symbol)
print(f"Amount invested: ${investment:.2f}")
