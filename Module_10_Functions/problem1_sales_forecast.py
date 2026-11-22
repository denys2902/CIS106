def forecast_sales(month, sales):
    month = month.strip().lower()[:3]
    if month in ('jan', 'feb', 'mar'):
        percent = 0.10
    elif month in ('apr', 'may', 'jun'):
        percent = 0.15
    elif month in ('jul', 'aug', 'sep'):
        percent = 0.20
    elif month in ('oct', 'nov', 'dec'):
        percent = 0.25
    else:
        raise ValueError('Unknown month')
    return sales * (1 + percent)

while input('Enter another record? (Yes or No): ').strip().lower() == 'yes':
    last_name = input('Last name: ')
    month = input('Month (Jan-Dec): ')
    sales = float(input('Current sales: $'))
    try:
        next_sales = forecast_sales(month, sales)
        print(f'{last_name}: next month forecast = ${next_sales:,.2f}')
    except ValueError:
        print('Invalid month. Please try again.')
