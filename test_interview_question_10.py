# Scenario:
# You have a dataset of locations representing parks, with their names and coordinates
#  stored in a CSV file. The goal is to load the data, filter parks within a specific latitude range,
#  and save the filtered data to a new file. Along the way, you'll need to perform basic error handling
#  and demonstrate understanding of Python data types and geospatial processing.

# Task:

# Write a Python script to:
# Read the data from a CSV file into a suitable data structure.
# Filter out parks with latitude values outside the range of 40 to 50.
# Save the filtered data to a new CSV file.
# For each park in the filtered dataset, use a library like shapely to create a point geometry object and print the park name with its coordinates.
# Include error handling for cases where:
# The input CSV file is missing or inaccessible.
# The latitude or longitude values are invalid (e.g., non-numeric or missing).
import csv
from shapely import Point

file_path = "q_10_data.csv"
valid_points = []
output = "q_10_answers.csv"
try:
    with open(file_path, "r") as file:
        data = csv.DictReader(file)
        for row in data:

            try:
                lat = float(row["Latitude"])
                lon = float(row["Longitude"])
                point = Point(lon, lat)
                row["geometry"] = point

                if 40 < lat < 50:
                    valid_points.append(row)
                    print(
                        f"Valid Latitude:\n     Park Name: {row['ParkName']}Park geometry: {row['geometry']}"
                    )

            except ValueError as ve:
                print(f"Error processing row {row}: {ve}")
            except Exception as e:
                print(f"Error: {e}")
        if valid_points:
            keys = valid_points[0].keys()
            with open(output, "w", newline="") as output_file:
                dict_writer = csv.DictWriter(output_file, keys)
                dict_writer.writeheader()
                dict_writer.writerows(valid_points)
except FileNotFoundError as fnfe:
    print(f"Error, File not found: {fnfe}")
except Exception as e:
    print(f"Error: {e}")
