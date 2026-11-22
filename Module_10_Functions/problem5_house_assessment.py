def assessed_value(county, market_value):
    county = county.strip().lower()
    if county == 'cook':
        percent = 0.90
    elif county == 'dupage':
        percent = 0.80
    elif county == 'mchenry':
        percent = 0.75
    elif county == 'kane':
        percent = 0.60
    else:
        percent = 0.70
    return market_value * percent

total_market = 0
total_assessed = 0
while input('Enter another house? (Yes or No): ').strip().lower() == 'yes':
    county = input('County: ')
    market = float(input('Market value: $'))
    assessed = assessed_value(county, market)
    print(f'{county}: assessed value = ${assessed:,.2f}')
    total_market += market
    total_assessed += assessed
print(f'Total market values: ${total_market:,.2f}')
print(f'Total assessed values: ${total_assessed:,.2f}')
