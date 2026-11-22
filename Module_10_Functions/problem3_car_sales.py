def car_sale_price(msrp, make, model, electric_code):
    make = make.strip().lower()
    model = model.strip().lower().replace(' ', '')
    if electric_code.strip().upper() == 'Y':
        discount = 0.30
    elif make == 'honda' and model == 'accord':
        discount = 0.10
    elif make == 'toyota' and model == 'rav4':
        discount = 0.15
    else:
        discount = 0.05
    return (msrp * (1 - discount)) * 1.07

total_msrp = 0
total_sales = 0
while input('Enter another vehicle? (Yes or No): ').strip().lower() == 'yes':
    make = input('Make: ')
    model = input('Model: ')
    electric = input('Electric vehicle? (Y or N): ')
    msrp = float(input('MSRP: $'))
    sale = car_sale_price(msrp, make, model, electric)
    print(f'{make} {model}: final price including 7% tax = ${sale:,.2f}')
    total_msrp += msrp
    total_sales += sale
print(f'Total MSRP: ${total_msrp:,.2f}')
print(f'Total sales prices (after discount and tax): ${total_sales:,.2f}')
