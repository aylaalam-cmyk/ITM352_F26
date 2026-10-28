# Read taxi_1000.csv and calculate fare and distance statistics for trips
# with fares greater than $10.
import csv
from pathlib import Path

filename = Path(__file__).resolve().with_name("taxi_1000.csv")

with open(filename, mode="r", newline="") as file:
    csv_reader = csv.reader(file)

    total_fare = 0
    max_distance = 0
    num_rows = 0
    qualifying_rows = 0

    for row in csv_reader:
        if num_rows == 0:
            # skip the header row
            fare_index = row.index("Fare")
            distance_index = row.index("Trip Miles")
            num_rows += 1
            continue

        fare = float(row[fare_index])
        distance = float(row[distance_index])

        if fare > 10:
            total_fare += fare
            if distance > max_distance:
                max_distance = distance
            qualifying_rows += 1

        num_rows += 1

average_fare = total_fare / qualifying_rows if qualifying_rows else 0

print(f"Total Fare: ${total_fare:.2f}")
print(f"Average Fare: ${average_fare:.2f}")
print(f"Max Trip Distance: {max_distance:.2f} miles")