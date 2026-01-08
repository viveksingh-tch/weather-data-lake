# 🌦️ Weather Data Lake (ETL Pipeline)

## 📖 Project Overview
This project builds a **Data Lake** foundation using Python. It extracts live weather data from the **Open-Meteo API** and stores it in an optimized, partitioned **Parquet** format.

It demonstrates the transition from simple file storage (CSV) to enterprise-grade Data Lake architectures (Hive Partitioning).

## 🏗️ Architecture
```mermaid
graph LR
    A[Public API: Open-Meteo] -->|JSON Response| B(Extraction Script)
    B -->|Pandas DataFrame| C{ETL Pipeline}
    C -->|Write Parquet| D[Data Lake Storage]
    D --> E[Partition: Year/Month/Day]

    🛠️ Tech Stack
Language: Python 3.10+

Data Source: Open-Meteo Public API (No Key Required)

Storage Format: Apache Parquet (Columnar Storage)

Partitioning Strategy: Hive-Style (key=value)

Libraries: Pandas, Requests, PyArrow

⚡ Key Features
API Integration: Handles HTTP requests and JSON parsing from a remote endpoint.

Schema Enforcement: Converts raw JSON into structured DataFrames with proper data types.

Optimized Storage: Uses Parquet for 70% better compression than CSV.

Partitioning: Implements year/month/day directory structures for efficient querying.

🚀 How to Run
Install Dependencies:
Bash
pip install pandas requests pyarrow

Run the Pipeline:
Bash
python pipeline.py

Verify the Data Lake:
# Read the Parquet files back into a readable table
python -c "import pandas as pd; print(pd.read_parquet('data/weather_lake').head())"
