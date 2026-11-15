total_tuition = 0.0
count = 0
with open("students.txt", "r") as file:
    while True:
        name = file.readline().strip()
        if not name:
            break
        district = file.readline().strip().upper()
        credits = int(file.readline().strip())
        rate = 250 if district == "I" else 500
        tuition = credits * rate
        total_tuition += tuition
        count += 1
        print(f"{name}: Credits {credits}, Tuition owed ${tuition:,.2f}")
print(f"Total tuition owed: ${total_tuition:,.2f}")
print(f"Number of students: {count}")
