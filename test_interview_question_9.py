# Scenario: You have been given a dataset of cities, each with a name, population, and geographic
# coordinates (latitude and longitude). Your task is to write a Python script to perform the following:

# Parse the data into an appropriate data structure.
# Identify cities with populations greater than a given threshold (e.g., 500,000) and print their names and coordinates.
# Handle any errors that may arise during data parsing or processing (e.g., missing or invalid values).
# Bonus: Using geopy, calculate and print the distance between two specified cities in the dataset.

import geopandas as gpd
import pandas as pd
import numpy as np
from shapely.geometry import Point

cities_data = [
    {
        "name": "New York",
        "population": 8419600,
        "coordinates": (40.7128, -74.0060),
    },
    {
        "name": "Los Angeles",
        "population": 3980400,
        "coordinates": (34.0522, -118.2437),
    },
    {
        "name": "Chicago",
        "population": 2716000,
        "coordinates": (41.8781, -87.6298),
    },
    {
        "name": "Houston",
        "population": 2328000,
        "coordinates": (29.7604, -95.3698),
    },
    {
        "name": "Phoenix",
        "population": None,
        "coordinates": (33.4484, -112.0740),
    },
    {"name": "San Diego", "population": 1407000, "coordinates": None},
]

df = pd.DataFrame.from_dict(cities_data)
if df.isnull().values.any():
    print(
        f"Malformed data: {df.isnull().sum().sum()} null values found. Dropping rows with null values."
    )

df = df.dropna(subset=["name", "population", "coordinates"])
df.reset_index(drop=True, inplace=True)

df["geometry"] = gpd.points_from_xy(
    df["coordinates"].str[1], df["coordinates"].str[0], crs="EPSG:4326"
)
df = df.drop(columns=["coordinates"])
gdf = gpd.GeoDataFrame(df, geometry="geometry")

gdf["> 500000"] = df["population"] > 500000
filtered_cities = gdf[gdf["> 500000"]][["name", "population"]]


from geopy.distance import geodesic


############# find distance with geopy
def find_distance(city_1, city_2):
    coords_1 = (city_1.y, city_1.x)
    coords_2 = (city_2.y, city_2.x)
    return geodesic(coords_1, coords_2).miles


############ Find distance with shapley #############
######## requires df["geometry"] = [Point(coord[1], coord[0]) for coord in df["coordinates"]]###########
gdf_projected = gdf.to_crs("EPSG:3395")  # World Mercator for distance in meters


# Define distance calculation
def find_distance_shapley(city_1, city_2):
    return city_1.distance(city_2) / 1000


city_1 = gdf.loc[1]["geometry"]
city_2 = gdf.loc[2]["geometry"]
print(city_2)
print(find_distance(city_1, city_2))
# print(filtered_cities)
