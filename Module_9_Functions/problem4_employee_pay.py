def pay_rate(job_code):
    if job_code == "L":
        return 25
    elif job_code == "A":
        return 30
    elif job_code == "J":
        return 50
    return 0


total_gross_pay = 0
while True:
    last_name = input("Enter employee last name (or stop): ")
    if last_name.lower() == "stop":
        break
    job_code = input("Enter job code (L, A, J): ").upper()
    hours = float(input("Enter hours worked: "))
    rate = pay_rate(job_code)
    if rate == 0:
        print("Invalid job code. Employee skipped.")
        continue
    if hours > 40:
        gross_pay = 40 * rate + (hours - 40) * rate * 1.5
    else:
        gross_pay = hours * rate
    print(f"Last name: {last_name}, Gross pay: ${gross_pay:.2f}")
    total_gross_pay += gross_pay

print(f"Total gross pay: ${total_gross_pay:.2f}")
