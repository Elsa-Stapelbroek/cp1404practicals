
print("Electricity bill estimator 2.0")

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
tariff_choice = input("Which tariff? 11 or 31: ")

while tariff_choice != "11" and tariff_choice != "31":
    print("Invalid tariff choice")
    tariff_choice = input("Which tariff? 11 or 31: ")

price_per_kwh = TARIFF_11 if tariff_choice == "11" else TARIFF_31
daily_use_kwh = float(input("Enter daily use in kWh: "))
number_of_billing_days = int(input("Enter number of billing days: "))
estimated_bill = price_per_kwh * daily_use_kwh * number_of_billing_days

print(f"Estimated bill: ${estimated_bill:.2f}")
