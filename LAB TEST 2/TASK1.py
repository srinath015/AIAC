def parse_and_aggregate_soil_moist(raw_text):
    """
    Parses CSV lines of tractor telemetry and computes per-tractor and overall soil moisture averages.
    Returns: (dict of {id: avg_soil_moist}, overall_avg)
    """
    from collections import defaultdict

    sums = defaultdict(float)
    counts = defaultdict(int)
    total_sum = 0.0
    total_count = 0

    for line in raw_text.strip().split('\n'):
        line = line.strip()
        if not line:
            continue
        parts = line.split(',')
        if len(parts) != 3:
            continue
        tractor_id, _, soil_moist_str = parts
        try:
            soil_moist = float(soil_moist_str)
        except ValueError:
            continue
        sums[tractor_id] += soil_moist
        counts[tractor_id] += 1
        total_sum += soil_moist
        total_count += 1

    avg_per_id = {}
    for tractor_id in sums:
        avg = round(sums[tractor_id] / counts[tractor_id], 2)
        avg_per_id[tractor_id] = avg

    overall_avg = round(total_sum / total_count, 2) if total_count else 0.0

    return avg_per_id, overall_avg

# Load and process the CSV file
if __name__ == "__main__":
    # Read the CSV file
    with open(r"C:\Users\pooda\OneDrive\Desktop\AIAC\LAB TEST 2\tractor_telemetry.csv", 'r') as file:
        csv_content = file.read()
    
    # Process the data
    avg_per_tractor, overall_average = parse_and_aggregate_soil_moist(csv_content)
    
    # Display results in the required format
    print(avg_per_tractor, f"and overall_avg={overall_average}")