# Question:

# You are tasked with writing a Python script to process a list of latitude and longitude coordinates stored in a text file and perform the following operations:

# Read the coordinates from a file named coordinates.txt. Each line in the file contains a pair of latitude and longitude values separated by a comma (e.g., 34.0522,-118.2437).
# Store the coordinates in an appropriate Python data structure for easy access and manipulation.
# Use the shapely library to create Point geometries for each coordinate.
# Check if each Point is within a predefined bounding box defined as follows:
# xmin = -125, ymin = 25, xmax = -65, ymax = 50.
# If the Point is inside the bounding box, store it in a list called valid_points.
# If the Point is outside, store it in a list called invalid_points.
# Handle any errors (e.g., malformed coordinate data in the file) gracefully and log the details to a file named errors.log.
# Tasks:

# Write the Python code to implement the above steps.
# Explain your choice of data structures and control flow in the script.
# Discuss how you would test this script to ensure it works as expected.
from shapely.geometry import Point
from shapely import Polygon
import matplotlib.pyplot as plt
import geopandas as gpd

with open("coordinates.txt", "r") as file:
    poly_coords = ((-125, 25), (-65, 25), (-65, 50), (-125, 50), (-125, 25))
    aoi_polygon = Polygon(poly_coords)
    coordinates = file.readlines()
    valid_points = []
    invalid_points = []
    for i in coordinates:
        i = i.strip("\n")
        i_list = i.split(",")

        try:
            x_coor = float(i_list[0])
            y_coor = float(i_list[1])
        except ValueError as ve:
            print(f"Error message: {ve}")
            with open("errors.log", "a") as errors:
                errors.write(f"Error message: {ve}\n")

        else:
            point = Point(x_coor, y_coor)

            if not point.within(aoi_polygon):
                invalid_points.append(point)
            else:
                valid_points.append(point)

    print(f"valid_points:\n     {valid_points}")
    print(f"invalid_points:\n     {invalid_points}")
    p = gpd.GeoSeries(aoi_polygon)
    p.plot()
    plt.show()
