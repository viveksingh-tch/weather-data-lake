import requests
import pandas as pd
from datetime import datetime

# 1. Define our "Source" Config (Lat/Lon for cities)
CITIES = {
    'London': {'lat': 51.5074, 'lon': -0.1278},
    'New_York': {'lat': 40.7128, 'lon': -74.0060},
    'Tokyo': {'lat': 35.6762, 'lon': 139.6503},
    'Mumbai': {'lat': 19.0760, 'lon': 72.8777},
    'Sydney': {'lat': -33.8688, 'lon': 151.2093}
}

API_URL = "https://api.open-meteo.com/v1/forecast"

def fetch_weather_data():
    all_data = []
    
    print(f"🌍 Starting Weather Extraction at {datetime.now()}")
    
    for city_name, coords in CITIES.items():
        # 2. Build the API Request
        params = {
            'latitude': coords['lat'],
            'longitude': coords['lon'],
            'current_weather': 'true'  # We only want real-time data
        }
        
        try:
            # 3. Hit the API (The "Handshake")
            response = requests.get(API_URL, params=params)
            data = response.json()
            
            # 4. Parse the specific fields we need
            current = data['current_weather']
            
            # Create a structured record
            record = {
                'city': city_name,
                'temperature': current['temperature'],
                'windspeed': current['windspeed'],
                'winddirection': current['winddirection'],
                'time': current['time'],
                'is_day': current.get('is_day', 0) # 1=Day, 0=Night
            }
            all_data.append(record)
            print(f"✅ Fetched data for {city_name}: {record['temperature']}°C")
            
        except Exception as e:
            print(f"❌ Failed to fetch {city_name}: {e}")

    # 5. Convert to DataFrame (The "Table")
    df = pd.DataFrame(all_data)
    
    # Add a timestamp for when *we* processed it
    df['ingestion_timestamp'] = datetime.now()
    
    return df

if __name__ == "__main__":
    # Test the function
    df = fetch_weather_data()
    print("\n📊 Raw Data Preview:")
    print(df.head(10))