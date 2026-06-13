# Project 10: Airflow + Snowflake Pipeline

## Overview
An orchestrated data pipeline using Apache Airflow that extracts weather data from Open-Meteo API and loads it into Snowflake cloud data warehouse.

## Pipeline Architecture
Open-Meteo API → Airflow DAG → Snowflake

## What it Does
- Extracts 7 days of weather data for Lahore via API
- Orchestrates extraction and loading as a 2-task DAG
- Loads data into Snowflake table
- Scheduled to run daily

## Tools & Technologies
| Tool | Purpose |
|------|---------|
| Apache Airflow | Pipeline orchestration |
| Docker | Running Airflow |
| Snowflake | Cloud data warehouse |
| Python | Pipeline logic |
| Open-Meteo API | Data source |

## DAG Structure
extract_weather >> load_to_snowflake

## How to Run
1. Start Airflow: `docker compose up`
2. Access UI: http://localhost:8080 (airflow/airflow)
3. Trigger DAG: `weather_to_snowflake`