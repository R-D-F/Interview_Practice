import geopandas as gpd

# Load the shapefile
try:
    data = gpd.read_file("city_parks.shp")
    # Check if required fields exist
    if not {"City", "Area"}.issubset(data.columns):
        raise ValueError("Missing required fields in shapefile!")
except Exception as e:
    print(f"Error loading shapefile: {e}")
    exit()

# Drop rows with missing values in 'City' or 'Area'
data = data.dropna(subset=["City", "Area"])

# Group by city and calculate total park area
output_df = data.groupby("City")["Area"].sum().reset_index()
print(output_df)
output_df.rename(columns={"Area": "Total_Area"}, inplace=False)

# Save to CSV
output_df.to_csv("city_park_area.csv", index=True)
print("Processed data saved to city_park_area.csv")
