-- This model selects and cleans columns from the raw titanic table
SELECT 
    survived,
    pclass AS passenger_class,
    sex,
    age,
    fare,
    embarked AS port_of_embarkation
FROM  `de-projects-499016.titanic_dataset.titanic_clean`