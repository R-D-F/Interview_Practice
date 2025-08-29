import arcpy


def describe_crs(shp_file: str) -> str:
    """Return a formatted description of the CRS for a shapefile,
    including whether it's geographic or projected."""

    spatial_ref = arcpy.Describe(shp_file).spatialReference

    # Check if it's geographic (degrees) or projected (linear units)
    if spatial_ref.type == "Geographic":
        coord_type = "Geographic (units: degrees)"
    else:
        coord_type = f"Projected (units: {spatial_ref.linearUnitName})"

    return (
        f"Name: {spatial_ref.name}\n"
        f"Factory Code (EPSG): {spatial_ref.factoryCode}\n"
        f"Type: {coord_type}"
    )


shp = r"condcutors_by_circuit\NG_191_115_05\NG_191_115_05_CONDUCTORS.shp"
print(describe_crs(shp))
