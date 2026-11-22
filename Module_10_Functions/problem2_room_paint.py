def wall_area(length, width, height):
    return 2 * length * height + 2 * width * height

def ceiling_area(length, width):
    return length * width

while input('Enter another room? (Yes or No): ').strip().lower() == 'yes':
    length = float(input('Room length (feet): '))
    width = float(input('Room width (feet): '))
    height = float(input('Room height (feet): '))
    walls = wall_area(length, width, height)
    gallons = walls / 50
    print(f'Wall area: {walls:.2f} square feet')
    print(f'Wall paint needed: {gallons:.2f} gallons')
    ceiling = ceiling_area(length, width)
    print(f'Ceiling/floor area (bonus): {ceiling:.2f} square feet')
    print(f'Ceiling paint/floor varnish (bonus): {ceiling / 50:.2f} gallons')
