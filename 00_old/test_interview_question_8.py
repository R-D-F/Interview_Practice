# Scenario: You have been provided with a list of point locations representing tree planting sites and need to ensure the data meets project specifications.
# The coordinates of each tree are provided as latitude and longitude pairs in a CSV file. Additionally, you must perform the following tasks:

# Validate that all coordinates are within the bounds of a specified region (bounding box). The bounding box for this project is:
# Min Latitude: 37.0
# Max Latitude: 38.0
# Min Longitude: -123.0
# Max Longitude: -121.0
# Count the number of valid and invalid points.
# Save the valid points as a GeoJSON file.
# Print any errors encountered during processing (e.g., malformed input or missing data).

import pandas as pd
import geopandas as gpd
from shapely import Polygon
import numpy

file_path = "question_8_data.csv"
bounding_box_coords = (
    (-123, 37),
    (-121, 37),
    (-121, 38),
    (-123, 38),
    (-123, 37),
)
aoi_polygon = Polygon(bounding_box_coords)


# get data from csv to pandas, then convert to geopandas
try:
    with open(file_path, "r") as file:
        df = pd.read_csv(file)

        df["Latitude"] = pd.to_numeric(df["Latitude"], errors="coerce")
        df["Longitude"] = pd.to_numeric(df["Longitude"], errors="coerce")

        if df.isnull().values.any():
            print(
                f"Malformed data: {df.isnull().sum().sum()} null values found. Dropping rows with null values."
            )

        df = df.dropna(subset=["Latitude", "Longitude"])
        df.reset_index(drop=True, inplace=True)

        df["geometry"] = gpd.points_from_xy(
            df["Longitude"], df["Latitude"], crs="EPSG:4326"
        )
        gdf = gpd.GeoDataFrame(df, geometry="geometry")
        gdf["within_polygon"] = gdf.within(aoi_polygon)
        counts = gdf["within_polygon"].value_counts()
        counts_of_true = counts[True]
        counts_of_false = counts[False]
        print(counts_of_true)
        print(counts_of_false)

        within_polygon_gdf = gdf[gdf["within_polygon"]]
        within_polygon_gdf.to_file("answer_8.geojson", driver="GeoJSON")
except FileNotFoundError as fnfe:
    print(f"File not found: {fnfe}")

    # print(gdf.head())
