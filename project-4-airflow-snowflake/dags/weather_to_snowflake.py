from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import requests
import pandas as pd

# Define default arguments for the DAG
default_args = {
    'owner': 'maham',
    'retries': '1',

}

# ============ EXTRACT FUNCTION ============
def extract_weather():
    """Fetch weather data from Open-Meteo API"""
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 31.5204,
        "longitude": 74.3587,
        "daily": ["temperature_2m_max", "temperature_2m_min", "precipitation_sum"],
        "timezone": "Asia/Karachi",
        "past_days": 7
    }
    response = requests.get(url, params=params)
    data = response.json()
    
    # Save to CSV so next task can read it
    daily = data["daily"]
    df = pd.DataFrame({
        "date": daily["time"],
        "temp_max": daily["temperature_2m_max"],
        "temp_min": daily["temperature_2m_min"],
        "precipitation": daily["precipitation_sum"]
    })
    df.to_csv("/opt/airflow/dags/weather_data.csv", index=False)
    print("Weather data extracted and saved!")

    
# ============ LOAD FUNCTION ============
def load_to_snowflake():
    """Load weather data into Snowflake"""
    import snowflake.connector
    
    df = pd.read_csv("/opt/airflow/dags/weather_data.csv")
    
    # Connect to Snowflake
    conn = snowflake.connector.connect(
        user='snowflake_user',
        password='snowflake_password',
        account='snowflake_account',
        database='TITANIC_DB',
        schema='PUBLIC'
    )
    
    cursor = conn.cursor()
    
    # Create table if not exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather_data (
            date DATE,
            temp_max FLOAT,
            temp_min FLOAT,
            precipitation FLOAT
        )
    """)
    
    # Insert data
    for _, row in df.iterrows():
        cursor.execute(
            "INSERT INTO weather_data VALUES (%s, %s, %s, %s)",
            (row['date'], row['temp_max'], row['temp_min'], row['precipitation'])
        )
    
    conn.commit()
    cursor.close()
    conn.close()
    print("Data loaded to Snowflake!")

# ============ DAG DEFINITION ============
with DAG(
    dag_id='weather_to_snowflake',
    default_args=default_args,
    description='Fetch weather data and load to Snowflake',
    schedule='@daily',
    start_date=datetime(2026, 1, 1),
    catchup=False,
) as dag:

    extract_task = PythonOperator(
        task_id='extract_weather',
        python_callable=extract_weather,
    )

    load_task = PythonOperator(
        task_id='load_to_snowflake',
        python_callable=load_to_snowflake,
    )

    extract_task >> load_task