count = 0
answer = input("Do you want to continue? Yes/No: ")
while answer.strip().lower() == "yes":
    last_name = input("Enter student last name: ")
    exam1 = float(input("Enter first exam score: "))
    exam2 = float(input("Enter second exam score: "))
    average = (exam1 + exam2) / 2
    count += 1
    print("Last Name:", last_name)
    print("Average:", round(average, 2))
    answer = input("Do you want to continue? Yes/No: ")
print("Number of students:", count)
