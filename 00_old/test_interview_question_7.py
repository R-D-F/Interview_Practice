# Task: Write a Python script that performs the following:

# Reads a provided dataset of points (latitude and longitude coordinates) from a CSV file.
# Filters the points to keep only those within a specified bounding box.
# Calculates the Euclidean distance from each point to a specified central location (given as latitude and longitude).
# Saves the filtered points and their calculated distances to a new CSV file.
# Handle any potential errors gracefully.
# Specify bounding box as [min_latitude, max_latitude, min_longitude, max_longitude]
from shapely import Polygon, Point
import geopandas as gpd
import pandas as pd

bounding_box = (
    (-130, 30),
    (-130, 40),
    (-70, 40),
    (-70, 30),
    (-130, 30),
)  # Example: Box covering part of the U.S.
central_location = (37.7749, -122.4194)  # Example: San Francisco, CA
aoi_polygon = Polygon(bounding_box)
reference_point = Point(central_location[1], central_location[0])
reference_point_proj = (
    gpd.GeoSeries([reference_point], crs="EPSG:4326").to_crs(epsg=3857).iloc[0]
)

print(reference_point_proj)

try:
    with open("data_7.csv", "r") as file:
        data = pd.read_csv(file)
        data["geometry"] = gpd.points_from_xy(
            data["Longitude"], data["Latitude"], crs="EPSG:4326"
        )
        geo_data = gpd.GeoDataFrame(data, geometry="geometry")
        filtered_points = geo_data[geo_data.intersects(aoi_polygon)]

        filtered_points = filtered_points.to_crs(3857)
        filtered_points["Distance"] = filtered_points.distance(
            reference_point_proj
        )
        filtered_points.to_csv("question_7_answer.csv")
except FileNotFoundError as fnfe:
    print(f"File specified does not exist: {fnfe}")
except Exception as e:
    print(f"Error: {e}")
