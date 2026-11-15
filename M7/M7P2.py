start = int(input("Enter start value: "))
stop = int(input("Enter stop value: "))
increment = int(input("Enter increment value: "))

if increment <= 0:
    print("Increment must be positive.")
else:
    number = start
    while number <= stop:
        print(number)
        number += increment
