def ticket_price(miles):
    if miles >= 30:
        return 12
    elif miles >= 20:
        return 10
    elif miles >= 10:
        return 8
    else:
        return 5

total = 0
while input('Enter another passenger? (Yes or No): ').strip().lower() == 'yes':
    last_name = input('Last name: ')
    miles = float(input('Miles from downtown Chicago: '))
    price = ticket_price(miles)
    print(f'{last_name}: ticket price = ${price:.2f}')
    total += price
print(f'Total ticket prices: ${total:.2f}')
