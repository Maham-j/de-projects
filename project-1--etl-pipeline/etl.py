import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from google.cloud import bigquery


print("Extracting data...")
df = pd.read_csv("titanic.csv")
print(f"Rows loaded: {len(df)}")
print(df.head())

print("\nTransforming data...")
df = df.drop_duplicates()
df['age'] = df['age'].fillna(df['age'].median())
df['embarked'] = df['embarked'].fillna(df['embarked'].mode()[0])
df['survived'] = df['survived'].astype(bool)
print(f"Rows after cleaning: {len(df)}")
#LOAD
print("\n Loading the parquet..")
table = pa.Table.from_pandas(df)
pq.write_table(table, "titanic clean parquet")
print("saved to titanic_clean.parquet")



