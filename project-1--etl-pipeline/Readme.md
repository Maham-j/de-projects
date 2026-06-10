# Project 1: ETL Pipeline - Titanic Dataset

## Overview
An end-to-end ETL pipeline that extracts data from a CSV file, 
cleans it using Python and Pandas, saves it in Parquet format, 
and loads it into Google BigQuery for cloud storage and analysis.

## Pipeline Architecture
CSV File → Extract → Transform → Parquet → Google BigQuery

## What it Does
- Extracts 891 rows from Titanic CSV dataset
- Cleans data: removes duplicates, fills null values, fixes data types
- Converts cleaned data to Parquet format (columnar, compressed)
- Loads Parquet file into Google BigQuery table

## Tools & Technologies
- Python 3.11
- Pandas (data cleaning)
- PyArrow (Parquet conversion)
- Google BigQuery (cloud data warehouse)
- Google Cloud SDK (authentication)

## Project Structure
project-1-etl-pipeline/
├── etl.py                  # Main ETL script
├── titanic_clean.parquet   # Cleaned output file
├── README.md               # Project documentation
└── .gitignore              # Git ignore rules

## How to Run
1. Install dependencies:
   pip install pandas pyarrow google-cloud-bigquery

2. Authenticate with Google Cloud:
   gcloud auth application-default login

3. Run the pipeline:
   python etl.py

## Output
- Local: titanic_clean.parquet
- Cloud: BigQuery table → titanic_dataset.titanic_clean
