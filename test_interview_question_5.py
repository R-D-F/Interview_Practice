# Question:
# You are tasked with writing a Python script to process a list of shapefiles stored in a directory.
# Each shapefile contains point features representing locations of sensors. For each shapefile, you need to perform the following steps:

# Read the shapefile and extract its point geometries and a specific attribute called SensorType.
# Group the features by SensorType and count the number of points in each group.
# Handle errors gracefully, such as if the SensorType attribute is missing or the shapefile is empty.
# Write the grouped counts to a CSV file named after the shapefile (e.g., sensors_summary_[shapefile_name].csv).
# Using Python, outline how you would:

# Read and process the shapefiles (hint: use libraries like arcpy or geopandas).
# Group the features and count them by attribute values.
# Implement error handling for the mentioned scenarios.
# Save the results to a CSV file.

import geopandas as gpd
from shapely.geometry import Point
import os

path = "example_shapefiles"
all_files = os.listdir(path)
shp_files = [f for f in all_files if ".shp" in f]


for f in shp_files:
    csv_name = f"sensor_summary_{f.replace(".shp", "")}.csv"
    try:
        data = gpd.read_file(os.path.join(path, f))
        # print(data.head())
        if data.empty:
            print(f"{f} is empty!")
        else:
            grouped = (
                data.groupby("SensorType").size().reset_index(name="Count")
            )

            grouped.to_csv(csv_name, index=False)
            print(f"Summary written to {csv_name}")

    except Exception as e:
        print(f"Error processing {f}: {e}")
