# Module 3 - Problem 2: Exam points
last_name = input("Enter your last name: ")
midterm = float(input("Enter midterm score (0-100): "))
final = float(input("Enter final exam score (0-100): "))

total_points = midterm * 0.40 + final * 0.60

print("Last name:", last_name)
print(f"Total exam points: {total_points:.2f}")
