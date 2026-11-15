principal = float(input("Enter principal amount: "))
rate = float(input("Enter interest rate (e.g. 0.10): "))
initial_principal = principal
print(f"{'Year':<6}{'Beginning Balance':>20}{'Ending Balance':>20}")
for year in range(1, 6):
    beginning = principal
    interest = beginning * rate
    principal = beginning + interest
    print(f"{year:<6}${beginning:>19,.2f}${principal:>19,.2f}")
print(f"Total interest earned: ${principal - initial_principal:,.2f}")
