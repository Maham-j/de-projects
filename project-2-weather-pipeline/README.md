# Project 2: Weather Data Pipeline

## Overview
A data pipeline that fetches real weather data from Open-Meteo API
for Lahore, Pakistan, transforms it using Pandas, and loads it
into a PostgreSQL database running inside Docker.

## Pipeline Architecture
Open-Meteo API → Extract → Transform → PostgreSQL (Docker)

## What it Does
- Fetches 37 days of weather data for Lahore from free API
- Transforms data into a clean DataFrame
- Adds temperature range calculation
- Loads data into PostgreSQL database inside Docker container

## Tools & Technologies
| Tool | Purpose |
|------|---------|
| Python 3.11 | Main programming language |
| Requests | API data extraction |
| Pandas | Data transformation |
| PostgreSQL | Database storage |
| Docker | Container for PostgreSQL |
| SQLAlchemy | Database connection |

## How to Run
1. Start PostgreSQL container:
```bash
docker run --name weather-db -e POSTGRES_USER=maham -e POSTGRES_PASSWORD=maham123 -e POSTGRES_DB=weatherdb -p 5432:5432 -d postgres
```

2. Install dependencies:
```bash
pip install requests pandas psycopg2-binary sqlalchemy
```

3. Run the pipeline:
```bash
python weather_pipeline.py
```

## Output
- PostgreSQL table: `weatherdb.weather_data`
- 37 rows of daily weather data for Lahore
