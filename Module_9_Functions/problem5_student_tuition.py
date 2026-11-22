def tuition_owed(credit_hours, district_code):
    if district_code == "I":
        return credit_hours * 250
    elif district_code == "O":
        return credit_hours * 550
    return 0


total_tuition = 0
while True:
    last_name = input("Enter student last name (or stop): ")
    if last_name.lower() == "stop":
        break
    credit_hours = float(input("Enter credit hours: "))
    district_code = input("Enter district code (I or O): ").upper()
    if district_code not in ("I", "O"):
        print("Invalid district code. Student skipped.")
        continue
    tuition = tuition_owed(credit_hours, district_code)
    print(f"Student: {last_name}, Tuition owed: ${tuition:.2f}")
    total_tuition += tuition

print(f"Total tuition owed: ${total_tuition:.2f}")
