name = input("Enter appliance name: ")
price = float(input("Enter appliance cost: "))

if price > 1000:
    warranty = price * 0.10
else:
    warranty = price * 0.05

total = price + warranty

print("Appliance:", name)
print("Cost:", price)
print("Warranty:", warranty)
print("Total:", total)