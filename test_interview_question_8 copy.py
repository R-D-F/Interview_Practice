import csv
import json
from shapely.geometry import Point
from shapely.geometry import box

# Bounding box
bounding_box = box(-123.0, 37.0, -121.0, 38.0)

# File paths (example)
input_csv = "tree_data.csv"
output_geojson = "valid_trees.geojson"

# Data storage
valid_points = []
invalid_points = []
errors = []

# Processing the data
with open(input_csv, mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        try:
            # Parse latitude and longitude
            lat = float(row["Latitude"])
            lon = float(row["Longitude"])
            point = Point(lon, lat)

            # Check if the point is within the bounding box
            if point.within(bounding_box):
                valid_points.append(
                    {
                        "type": "Feature",
                        "geometry": {
                            "type": "Point",
                            "coordinates": [lon, lat],
                        },
                        "properties": {"TreeID": row["TreeID"]},
                    }
                )
            else:
                invalid_points.append(row)

        except (ValueError, KeyError) as e:
            errors.append(f"Error processing row {row}: {e}")

# Save valid points to GeoJSON
geojson_data = {"type": "FeatureCollection", "features": valid_points}

with open(output_geojson, mode="w") as file:
    json.dump(geojson_data, file, indent=2)

# Output results
print(f"Valid Points: {len(valid_points)}")
print(f"Invalid Points: {len(invalid_points)}")
if errors:
    print("Errors encountered:")
    for error in errors:
        print(error)
