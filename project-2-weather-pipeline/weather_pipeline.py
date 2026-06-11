import requests
import pandas as pd
from sqlalchemy import create_engine

# ============ EXTRACT ============
print("Extracting weather data from API...")

# Open-Meteo API - free, no API key needed
url = "https://api.open-meteo.com/v1/forecast"

# Parameters for Lahore, Pakistan
params = {
    "latitude": 31.5204,
    "longitude": 74.3587,
    "daily": ["temperature_2m_max", "temperature_2m_min", "precipitation_sum"],
    "timezone": "Asia/Karachi",
    "past_days": 30
}

response = requests.get(url, params=params)
data = response.json()
print("Data extracted successfully!")
print(data)


# ============ TRANSFORM ============
print("\nTransforming data...")

# Extract the daily data from response
daily = data["daily"]

# Create a DataFrame
df = pd.DataFrame({
    "date": daily["time"],
    "temp_max": daily["temperature_2m_max"],
    "temp_min": daily["temperature_2m_min"],
    "precipitation": daily["precipitation_sum"]
})

# Convert date column to datetime format
df["date"] = pd.to_datetime(df["date"])

# Add a column for temperature range
df["temp_range"] = df["temp_max"] - df["temp_min"]

print(f"Rows transformed: {len(df)}")
print(df.head())

# ============ LOAD ============
print("\nLoading data to PostgreSQL")

# Create connection to PostgreSQL running in Docker
engine = create_engine("postgresql://maham:maham123@localhost:5432/weatherdb")

# Load DataFrame to PostgreSQL table
df.to_sql("weather_data", engine, if_exists="replace", index="False")

print(f"Loaded {len(df)} rows to PostgreSQL table: weather_data ")
