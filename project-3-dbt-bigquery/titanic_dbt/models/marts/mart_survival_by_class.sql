-- This model analyzes survival rates by passenger class
SELECT
    passenger_class,
    COUNT(*) AS total_passengers,
    SUM(CASE WHEN survived = true THEN 1 ELSE 0 END) AS survivors,
    ROUND(SUM(CASE WHEN survived = true THEN 1 ELSE 0 END) / COUNT(*) * 100, 2) AS survival_rate_pct,
    ROUND(AVG(fare), 2) AS avg_fare
FROM {{ ref('stg_titanic') }}
GROUP BY passenger_class
ORDER BY passenger_class
