def calculate_bill():
    print("Electricity Bill Calculator")
    house_number = input("Enter your house number: ")
    try:
        previous_units = float(input("Enter previous meter reading (units): "))
        present_units = float(input("Enter present meter reading (units): "))
        if present_units < previous_units:
            print("Error: Present units cannot be less than previous units.")
            return
    except ValueError:
        print("Invalid input for units. Please enter numeric values.")
        return

    print("Purpose options:\n1. Domestic\n2. Industrial")
    purpose = input("Enter the purpose (Domestic/Industrial): ").strip().lower()

    if purpose == "domestic":
        rate = 5.0  # Example rate per unit for domestic
    elif purpose == "industrial":
        rate = 8.0  # Example rate per unit for industrial
    else:
        print("Invalid purpose entered. Please enter 'Domestic' or 'Industrial'.")
        return

    print(f"\nStep 1: House Number: {house_number}")
    print(f"Step 2: Previous Units: {previous_units}")
    print(f"Step 3: Present Units: {present_units}")
    units_consumed = present_units - previous_units
    print(f"Step 4: Units Consumed = Present Units - Previous Units = {present_units} - {previous_units} = {units_consumed}")
    print(f"Step 5: Purpose: {purpose.capitalize()}")
    print(f"Step 6: Rate per unit: {rate} currency/unit")
    bill_amount = units_consumed * rate
    print(f"Step 7: Bill Amount = Units Consumed x Rate = {units_consumed} x {rate} = {bill_amount} currency")
    print(f"\nTotal Electricity Bill for House {house_number}: {bill_amount} currency")

if __name__ == "__main__":
    calculate_bill()
