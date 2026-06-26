
# Project 9: Data Modeling with dbt + BigQuery

## Overview
A dbt project that transforms raw Titanic data from BigQuery into clean staging and mart models, with automated data quality tests.

## Pipeline Architecture
Raw BigQuery table → dbt staging model → dbt mart model → Business insights

## What it Does
- Creates staging model (stg_titanic) with renamed, cleaned columns
- Creates mart model (mart_survival_by_class) analyzing survival rates by passenger class
- Runs automated tests for data quality (not_null checks)
- Documents all models and columns

## Key Insight
1st class passengers had 63% survival rate vs 25% for 3rd class - showing wealth inequality in survival outcomes.

## Tools & Technologies
| Tool | Purpose |
|------|---------|
| dbt Core | Data transformation & modeling |
| Google BigQuery | Cloud data warehouse |
| SQL | Transformation logic |

## Project Structure
```
titanic_dbt/
├── models/
│   ├── staging/
│   │   ├── stg_titanic.sql
│   │   └── schema.yml
│   └── marts/
│       └── mart_survival_by_class.sql
├── dbt_project.yml
└── README.md
```

## How to Run
1. Install dbt: `pip install dbt-bigquery`
2. Authenticate: `gcloud auth application-default login`
3. Run models: `dbt run`
4. Run tests: `dbt test`
```


