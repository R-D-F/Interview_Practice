# Question
# You are tasked with writing a Python script to process a shapefile of city parks. The goal is to calculate the total area of parks for each city in the dataset, handle potential errors in the data, and save the results to a CSV file.

# The shapefile has the following attributes:

# City (string): Name of the city
# Park_Name (string): Name of the park
# Area (float): Area of the park in square meters
# Part 1: Data Handling and Control Flow
# Explain how you would iterate over the rows in the shapefile to group the parks by city and calculate the total park area for each city.
# Which Python data structures would you use to store the intermediate results, and why?
# Part 2: Error Handling
# Discuss how you would handle the following potential errors:
# Missing or null values in the City or Area fields.
# A shapefile that is not in the expected format (e.g., missing fields or corrupted file).
# Part 3: Geospatial Processing
# Write a Python code snippet using geopandas to:

# Read the shapefile.
# Calculate the total park area for each city.
# Save the results to a CSV file named city_park_areas.csv with the columns City and Total_Area.
# Bonus: Optimization and Validation
# How would you optimize the script for a shapefile with thousands of records?
# Describe one way to validate that the areas in the shapefile are calculated correctly.
import geopandas as gpd
import csv

data_dict = {}
filepath = "city_parks.shp"
try:
    data = gpd.read_file(filepath)
    if not {"City", "Area"}.issubset(data.columns):
        raise ValueError("Missing required fields in shapefile!")
except Exception as e:
    print(f"Error loading shapefile: {e}")
unique_cities = data["City"].unique()
output_dict = {}
for i in unique_cities:
    output_dict[i] = {"sum_park_area": 0}
for index, row in data.iterrows():
    try:
        city = row["City"]
        output_dict[city]["sum_park_area"] += row["Area"]

    except Exception as e:
        print(f"there was an error: {e}")

with open("city_park_area.csv", "w") as file:
    field_names = ["City", "Total_Area"]
    writer = csv.writer(file)
    writer.writerow(field_names)

    for key, value in output_dict.items():

        writer.writerow([key, value["sum_park_area"]])

# data_dict = data.to_dict()
# print(data_dict)
