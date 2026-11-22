def miles_per_gallon(miles, gallons):
    if gallons == 0:
        return 0
    return miles / gallons


trip_count = 0
while True:
    city = input("Enter destination city (or stop): ")
    if city.lower() == "stop":
        break
    miles = float(input("Enter miles traveled: "))
    gallons = float(input("Enter gallons used: "))
    mpg = miles_per_gallon(miles, gallons)
    print(f"City: {city}, Miles: {miles:.1f}, MPG: {mpg:.2f}")
    trip_count += 1

print(f"Number of trips: {trip_count}")
