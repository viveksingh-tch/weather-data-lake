from src.extract import fetch_weather_data
from src.store import save_to_datalake
import time

def run_pipeline():
    print("🚀 Starting Weather ETL Pipeline...")
    
    # Step 1: Extract (Get data from API)
    weather_df = fetch_weather_data()
    
    # Step 2: Load (Save to Parquet Lake)
    if not weather_df.empty:
        save_to_datalake(weather_df)
    else:
        print("⚠️ No data fetched, skipping save.")
        
    print("🏁 Pipeline Finished.")

if __name__ == "__main__":
    run_pipeline()