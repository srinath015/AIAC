def convert_temperature(value, from_unit, to_unit):
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    # Convert input to Celsius first
    if from_unit == 'c':
        celsius = value
    elif from_unit == 'f':
        celsius = (value - 32) * 5/9
    elif from_unit == 'k':
        celsius = value - 273.15
    else:
        raise ValueError("Unknown temperature unit: " + from_unit)

    # Convert from Celsius to target unit
    if to_unit == 'c':
        return celsius
    elif to_unit == 'f':
        return celsius * 9/5 + 32
    elif to_unit == 'k':
        return celsius + 273.15
    else:
        raise ValueError("Unknown temperature unit: " + to_unit)

def parse_input(user_input):
    # Example: "20 c", "30 f", "273.15 k"
    user_input = user_input.strip().lower()
    parts = user_input.split()
    if len(parts) != 2:
        raise ValueError("Input must be in the format: <value> <unit>")
    try:
        value = float(parts[0])
    except ValueError:
        raise ValueError("Temperature value must be a number.")
    unit = parts[1]
    if unit not in ['c', 'f', 'k']:
        raise ValueError("Unit must be 'c', 'f', or 'k'.")
    return value, unit

def main():
    print("Temperature Converter (Celsius, Fahrenheit, Kelvin)")
    print("Enter temperature (e.g., 20 c, 68 f, 300 k):")
    user_input = input().strip()
    try:
        value, from_unit = parse_input(user_input)
    except ValueError as e:
        print("Error:", e)
        return

    print("Convert to which unit? (c/f/k):")
    to_unit = input().strip().lower()
    if to_unit not in ['c', 'f', 'k']:
        print("Invalid target unit.")
        return

    if from_unit == to_unit:
        print(f"{value} {from_unit} = {value} {to_unit}")
        return

    try:
        result = convert_temperature(value, from_unit, to_unit)
        # Format result to 2 decimal places if not integer
        if result == int(result):
            result_str = str(int(result))
        else: