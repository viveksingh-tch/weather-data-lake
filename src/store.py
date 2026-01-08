import pandas as pd
import os
from datetime import datetime

def save_to_datalake(df):
    # 1. Add Partition Columns
    # We derive these from the timestamp so we can organize folders
    df['year'] = df['ingestion_timestamp'].dt.year
    df['month'] = df['ingestion_timestamp'].dt.month
    df['day'] = df['ingestion_timestamp'].dt.day
    
    # 2. Define the Base Path
    base_path = 'data/weather_lake'
    
    # 3. Save as Parquet with Partitioning
    # This automatically creates folders like: data/weather_lake/year=2024/month=01/...
    print(f"💾 Saving data to Data Lake at: {base_path}...")
    
    df.to_parquet(
        base_path,
        engine='pyarrow',
        partition_cols=['year', 'month', 'day'],
        index=False
    )
    
    print("✅ Data successfully saved to Parquet format!")

if __name__ == "__main__":
    # Dummy test
    print("Run pipeline.py instead!")