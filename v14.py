# For this exercise you can use the IDE of your choice and any resources you'd like. However,
# you should be prepared to explain your work and thought process.

# Create a Python script with as many functions as needed that performs the following operations:

# Directory Scanning and File Collection
#     - Recursively searches a given directory and its subdirectories to identify all shapefiles
#     - Stores the shapefile paths in an appropriate iterable data structure
#     - Handles potential errors gracefully (e.g., permission issues, corrupted files)

# Spatial Data Processing
#     - Reads each shapefile using an appropriate library (e.g., geopandas, arcpy)
#     - Creates a 100 meter buffer around each geometry
#     - The buffer distance should be parameterized
#     - Ensures proper handling of different coordinate reference systems (CRS)

# Area Calculation
#     - Calculates the total area of all buffered geometries
#     - Implements a solution to prevent double-counting of overlapping areas
#     - Returns the result in square meters

import os
import arcpy
import shutil


def reset_folder(folder_path: str):
    """Delete folder if it exists, then recreate it empty."""
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)  # deletes folder and all its contents
    os.makedirs(folder_path)  # recreate empty folder


def identify_shp_files(folder_path: str) -> list[str]:
    """Walk through a folder and return a list of all shape file paths.

    Args:
        Folder_path (str): The root folder to search.

    Returns:
        List[str]: A list of ful paths to all '.shp' files found
    """
    shp_files = []
    try:
        for dirpath, dirnames, filenames in os.walk(
            folder_path, onerror=lambda e: None
        ):
            for file in filenames:
                try:
                    if file.lower().endswith(".shp"):
                        shp_files.append(os.path.join(dirpath, file))
                except OSError as e:
                    print(f"Skipping file due to error: {file} ({e})")
    except Exception as e:
        print(f"Error walking directory {folder_path}")

    return shp_files


def apply_buffer(
    shp_file: str, output_folder: str, buffer_distance: float
) -> str:
    """takes a shape file input, applies a buffer (m) to it, returns result in ouput folder

    Args:
        shp_file (str): path to shape file
        output_folder (str): path to output folder
        buffer_distance (float): buffer distance in meters


    Returns:
        shp file of buffer at specified output path
    """
    file_name = os.path.basename(shp_file)
    base, ext = os.path.splitext(file_name)
    new_name = f"{base}_buffer{ext}"

    output_file_path = os.path.join(output_folder, new_name)

    arcpy.analysis.Buffer(
        in_features=shp_file,
        out_feature_class=output_file_path,
        buffer_distance_or_field=buffer_distance,
    )


def merge_polygons(folder_path, output):
    shp_files = []
    for (
        dirpath,
        dirnames,
        filenames,
    ) in os.walk(folder_path, onerror=lambda e: None):
        for file in filenames:
            if file.lower().endswith("_buffer.shp"):
                shp_files.append(os.path.join(dirpath, file))
    output_shp = os.path.join(output, "merged.shp")
    arcpy.Merge_management(shp_files, output_shp)


def dissolve_polygons(input_merge_folder, output_folder):
    # Make sure output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Path to final dissolved shapefile
    output_shp = os.path.join(output_folder, "dissolved.shp")

    # Find merged shapefile in input folder
    merged_shp = None
    for file in os.listdir(input_merge_folder):
        if file.endswith(".shp") and "merged" in file:
            merged_shp = os.path.join(input_merge_folder, file)
            break

    if merged_shp is None:
        raise FileNotFoundError("No merged shapefile found to dissolve.")

    # Dissolve all polygons into single multipart polygon
    arcpy.Dissolve_management(
        in_features=merged_shp,
        out_feature_class=output_shp,
        multi_part="MULTI_PART",
    )

    # Add area field
    arcpy.AddField_management(output_shp, "Area_m2", "DOUBLE")

    return output_shp


def calculate_area(shp_file):
    """Takes a shape file and calculates the area of it in the attribute table"""

    arcpy.CalculateGeometryAttributes_management(
        in_features=shp_file,
        geometry_property=[["Area_m2", "AREA"]],
        area_unit="SQUARE_METERS",
    )


def alternative_calculate_area(shp_file):
    total_area = 0
    with arcpy.da.SearchCursor(shp_file, ["SHAPE@AREA"]) as cursor:
        for row in cursor:
            total_area += row[0]
    return total_area


output_folder = r"D:\Interview_Practice\output"

directory_path = "condcutors_by_circuit"


reset_folder(r"D:\Interview_Practice\output")

shp_files = identify_shp_files(directory_path)
for file in shp_files:
    apply_buffer(file, output_folder, 100)

merge_polygons(output_folder, output_folder)
dissolved_file = dissolve_polygons(output_folder, output_folder)
calculate_area(dissolved_file)
