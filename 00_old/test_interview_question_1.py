# Interview Question for Junior GIS Developer:
# Question:

# You are given a CSV file containing the following columns: id, latitude, longitude, and land_use. Write a Python script that:

# Reads the CSV file into memory.
# Converts the latitude and longitude columns into point geometries using the shapely library.
# Groups the points by land_use and calculates the total count of points for each land_use.
# Handles any potential errors, such as missing values in the latitude or longitude columns, and logs them appropriately.
# Follow-up Questions:

# Which Python data structures would you use to store the geometries and group them by land_use?
# What type of control flow (e.g., loops, conditionals) do you think is needed for this task?
# How would you handle invalid or corrupted data in the CSV file?
# Can you extend the script to export the grouped results into a new CSV file?
# This question assesses the candidate's ability to:

# Understand and use Python data types like dictionaries or lists.
# Write control flow statements for grouping and processing data.
# Handle errors gracefully using try-except blocks.
# Use geospatial libraries like shapely for basic operations.


import csv
from shapely.geometry import Point

# Reads the CSV file into memory.
data_dict = []
with open("sample_data.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)

    for line in reader:
        try:
            lat = float(line[1])
            long = float(line[2])
            if not (-90 <= lat <= 90 and -180 <= long <= 180):
                raise ValueError(f"Invalid lat/long values {lat} {long}")
            data_dict.append(
                {
                    "id": line[0],
                    "lat": line[1],
                    "long": line[2],
                    "land_use": line[3],
                }
            )
        except ValueError as ve:
            print(f"ValueError for row {line[0]}: {ve}")
print(data_dict)

# Converts the latitude and longitude columns into point geometries using the shapely library.
for i in data_dict:
    point = Point(float(i["lat"]), float(i["long"]))
    i["point"] = point

# Groups the points by land_use and calculates the total count of points for each land_use.

land_use_list = []
land_use_dict = {}
for i in data_dict:
    if i["land_use"] not in land_use_list:
        land_use_list.append(i["land_use"])
print(land_use_list)
for i in land_use_list:
    land_use_dict[i] = {"points": [], "count": 0}
print(land_use_dict)
for i in data_dict:
    land_use_dict[i["land_use"]]["count"] += 1
    land_use_dict[i["land_use"]]["points"].append(i["point"])
# Handles any potential errors, such as missing values in the latitude or longitude columns, and logs them appropriately.
print(land_use_dict)
