# Question:
# You are tasked with processing geospatial data to analyze the total length of roads within a certain area of interest (AOI). Use Python to perform the following steps:

# Data Handling: Write a function that takes a list of road lengths (in kilometers) and returns a dictionary where the keys are ranges of lengths (e.g., "0-5 km", "5-10 km")
# and the values are counts of roads in each range. Use appropriate Python data structures.

# Control Flow: In the same function, include error handling to ensure that all inputs are numeric and non-negative. Raise a ValueError with a clear message if this condition is not met.

# Geoprocessing:
# Using a library like shapely or geopandas, describe (or pseudo-code) how you would filter roads that fall inside the AOI and calculate their total length. Assume you are provided:

# A GeoDataFrame of roads with geometry and length attributes.
# A Polygon object representing the AOI.
# Error Handling (Bonus): How would you handle cases where the input GeoDataFrame or AOI is missing or invalid?
from shapely.geometry import Polygon
import geopandas as gpd
import math

road_lengths = [
    1.2,
    3.5,
    7.8,
    5.5,
    2.1,
    10.4,
    8.3,
    12.0,
    # -3.5,
]  # Includes an invalid negative value for testing


# Define an AOI polygon
aoi_polygon = Polygon([(0, 0), (2, 0), (2, 2), (0, 2), (0, 0)])  # A square AOI


def rl_dict(road_lengths):
    road_lengths_dict = {}
    for i in road_lengths:
        if i <= 0:
            raise ValueError(f"Road_Length contains an unacceptable value: {i}")

        rd_len_div_five = i / 5
        pot_key = f"{(math.ceil(rd_len_div_five)*5)-5}-{math.ceil(rd_len_div_five)*5}km"
        if pot_key in road_lengths_dict:
            road_lengths_dict[pot_key] += 1
        else:
            road_lengths_dict[pot_key] = 1

    return road_lengths_dict


print(rl_dict(road_lengths))

try:
    road_data = gpd.read_file("roads.shp")

except Exception as e:
    print(f"Error loading shapefile: {e}")

aoi_roads = road_data[road_data.intersects(aoi_polygon)]
total_length = aoi_roads["length_km"].sum()
print(total_length)
print(aoi_roads)
