last_name = input("Enter last name: ")
salary = float(input("Enter salary: "))
job_level = int(input("Enter job level: "))

if job_level >= 10:
    rate = 0.25
elif job_level >= 5:
    rate = 0.20
else:
    rate = 0.10

bonus = salary * rate

print("Last name:", last_name)
print(f"Bonus: ${bonus:.2f}")