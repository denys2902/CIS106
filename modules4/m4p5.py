
# Module 4 - Problem 5
fixed_costs = float(input("Enter fixed costs: "))
price = float(input("Enter price per unit: "))
cost = float(input("Enter cost per unit: "))

break_even = fixed_costs / (price - cost)

print(f"Break-even point: {break_even:.2f} units")
