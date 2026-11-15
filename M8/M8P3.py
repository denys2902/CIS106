total_bonus = 0.0
with open("employees.txt", "r") as file:
    while True:
        name = file.readline().strip()
        if not name:
            break
        salary = float(file.readline().strip())
        if salary >= 100000:
            rate = 0.20
        elif salary >= 50000:
            rate = 0.15
        else:
            rate = 0.10
        bonus = salary * rate
        total_bonus += bonus
        print(f"{name}: Salary ${salary:,.2f}, Bonus ${bonus:,.2f}")
print(f"Total bonuses paid: ${total_bonus:,.2f}")
