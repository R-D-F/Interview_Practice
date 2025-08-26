# You are tasked with creating a Python script that performs the following operations:

# Read geospatial point data from a given file (in CSV format). Each row contains an ID, a latitude, and a longitude.
# Filter the points to only include those within a specific bounding box
# (e.g., latitudes between 30 and 40, and longitudes between -120 and -110).
# Write the filtered points to a new CSV file,
# adding a new column called Distance which calculates the distance (in kilometers) from a reference point (latitude: 35.0, longitude: -115.0).
# Handle potential errors such as missing files or invalid data gracefully.
import geopandas as gpd
import csv
from shapely.geometry import Polygon, Point
import matplotlib.pyplot as plt
import pandas

poly_coords = ((-120, 30), (-110, 30), (-110, 40), (-120, 40), (-120, 30))
reference_point = Point(-115, 35)
aoi_polygon = Polygon(poly_coords)
with open("sample_data_6.csv", "r") as file:
    # get csv into pandas df
    data = pandas.read_csv(file)

    # convert pandas df to geopandas
    data["geometry"] = gpd.points_from_xy(data["Longitude"], data["Latitude"])
    geo_data = gpd.GeoDataFrame(data, geometry="geometry")

    within_points = geo_data[geo_data.within(aoi_polygon)]
    within_points["distance"] = within_points.distance(reference_point)
    print(within_points)
    # within_points.to_csv("test_6_answer.csv")


#     geo_data.plot()
#     plt.show()

# p = gpd.GeoSeries(aoi_polygon)
# p.plot()
# plt.show()
