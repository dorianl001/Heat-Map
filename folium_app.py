import folium
from folium.plugins import HeatMap
import pandas as pd

# Step 1: Define your data
data = pd.DataFrame({
    'lat': [37.7749, 34.0522, 40.7128, 41.8781],
    'lon': [-122.4194, -118.2437, -74.0060, -87.6298],
    'weight': [0.6, 0.8, 0.9, 0.7]
})

# Step 2: Convert to heatmap data format
heat_data = [[row['lat'], row['lon'], row['weight']] for index, row in data.iterrows()]

# Step 3: Create the base map
m = folium.Map(location=[39.8283, -98.5795], zoom_start=4)

# Step 4: Add the heatmap layer
HeatMap(heat_data).add_to(m)

# Step 5: Save to HTML
m.save("geospatial_heatmap.html")

print("✅ Heatmap saved as geospatial_heatmap.html")

