# Q2. Dictionary & string formatting
# You’re given a dictionary of image metadata:

metadata = {
    "file": "tile_23.tif",
    "resolution": 0.5,
    "projection": "EPSG:26910",
    "bands": 4,
}

# 👉 Print a human-readable summary like:
# File tile_23.tif has 4 bands at 0.5m resolution using EPSG:26910 projection.


def summary(data: dict) -> str:
    """Returns human readable summary of metadata"""

    file = data["file"]
    resolution = data["resolution"]
    projection = data["projection"]
    bands = data["bands"]

    output = f"File {file} has {str(bands)} bands at {str(resolution)} resolution using {projection} projection."
    return output


print(summary(metadata))
