# Q3. Error handling
# Write a function that opens a .tif file using rasterio and returns its CRS. If the file doesn’t exist, return "File not found".

import os
import rasterio


def open_tif(tif_path: str) -> None:
    try:
        with rasterio.open(tif_path) as src:
            # Access metadata and properties of the dataset
            print(f"Driver: {src.driver}")
            print(f"CRS: {src.crs}")
            print(f"Bounds: {src.bounds}")
            print(f"Width: {src.width}")
            print(f"Height: {src.height}")
            print(f"Number of bands: {src.count}")
            print(f"Data type: {src.dtypes}")

            # Read the raster data from a specific band (e.g., band 1)
            # The data is returned as a NumPy array
            band_data = src.read(1)
            print(f"Shape of band 1 data: {band_data.shape}")
    except rasterio.errors.RasterioIOError:
        print("File not found")


open_tif(r"v13_data.tif")
