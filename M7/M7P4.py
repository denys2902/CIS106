total_pay = 0.0
count = 0
answer = input("Do you want to continue? Yes/No: ")
while answer.strip().lower() == "yes":
    last_name = input("Enter employee last name: ")
    hours = float(input("Enter hours worked: "))
    rate = float(input("Enter hourly rate: "))
    if hours > 40:
        gross_pay = 40 * rate + (hours - 40) * rate * 1.5
    else:
        gross_pay = hours * rate
    total_pay += gross_pay
    count += 1
    print("Last Name:", last_name)
    print(f"Gross Pay: ${gross_pay:.2f}")
    answer = input("Do you want to continue? Yes/No: ")
print(f"Total Gross Pay: ${total_pay:.2f}")
print("Number of Employees:", count)
if count > 0:
    print(f"Average Pay: ${total_pay / count:.2f}")
else:
    print("Average Pay: N/A (no employees)")
