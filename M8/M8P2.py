first = 1
second = 1
for number in range(20):
    print(first)
    first, second = second, first + second
