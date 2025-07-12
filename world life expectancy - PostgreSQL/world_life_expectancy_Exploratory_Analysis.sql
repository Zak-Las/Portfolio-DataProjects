-- World Life Expectancy (Exploratory Analysis)
-- To maintain clarity, the data clearning has been performed in a different script.

SELECT *
FROM worldlifeexpectancy
;

-- First, I am interested to see how the life expectancy of each country behaved between 2007 and 2022.
-- Identify the min and max values for life_expectancy

SELECT 
country, 
MIN(life_expectancy) AS min_life_expectancy,
MAX(life_expectancy) AS max_life_expectancy
FROM worldlifeexpectancy
GROUP BY country
ORDER BY country DESC 
;

-- Remark: there are many countries, like San Marino, who have '0' as their min and/or max life expectancy. 
-- This could be an issue with the data quality. For the time being, I will filter out these instances.

SELECT 
country, 
MIN(life_expectancy) AS min_life_expectancy,
MAX(life_expectancy) AS max_life_expectancy
FROM worldlifeexpectancy
GROUP BY country
HAVING MIN(life_expectancy) <> 0
AND MAX(life_expectancy) <> 0
ORDER BY country DESC 
;


-- Now I want to see which which countries have the largest difference between the min and max values

SELECT 
country, 
MIN(life_expectancy) AS min_life_expectancy,
MAX(life_expectancy) AS max_life_expectancy,
ROUND(MAX(life_expectancy)::numeric - MIN(life_expectancy)::numeric, 2) AS life_expec_diff
FROM worldlifeexpectancy
GROUP BY country
HAVING MIN(life_expectancy) <> 0
	AND MAX(life_expectancy) <> 0
ORDER BY life_expec_diff ASC 
;


-- Now I want to see the average life expectancy for each year

SELECT "year" , ROUND(AVG(life_expectancy::numeric),2)
FROM worldlifeexpectancy
WHERE life_expectancy != 0
GROUP BY "year" 
ORDER BY "year" ASC
;

-- Observation: The world as whole increased the global life expectancy from 66.75 in 2007 to 71.62 in 2022.

-- I want to take another look at the whole table to see if I can identify correlations between the different columns.

SELECT *
FROM worldlifeexpectancy
;

-- The most obvious suspects to be correlated to the life expectancy column are the BMI and GDP columns
-- I want to check if there is a correlation between the life expectancy and the GDP of each country 

SELECT country, ROUND(AVG(life_expectancy),2) AS avg_life_expec, ROUND(AVG(gdp),2) AS avg_gdp
FROM worldlifeexpectancy
GROUP BY country 
HAVING ROUND(AVG(life_expectancy),2) > 0
	AND ROUND(AVG(gdp),2) > 0
ORDER BY avg_gdp ASC 
;

-- Many countries do not have data for their GDP. So, I filltered those instances out.
-- The query above can be fed to visualization tool to see a positive correlation between life expectancy and gdp.

-- Now I was to split the values of life expectancy and dgp between two categories: High and Low.
-- I want to see if data puts each country in the 'High' category for both life expectancy and dgp, and vis versa for the 'Low' category

SELECT 
SUM(CASE 
	WHEN gdp > 1500 THEN 1 -- roughly this is the mid value for the dataset
	ELSE 0  
END) AS high_gdp_count,
ROUND(AVG(CASE 
	WHEN gdp > 1500 THEN life_expectancy  -- roughly this is the mid value for the dataset
	ELSE NULL  
END), 2) AS high_gdp_life_expec,
SUM(CASE 
	WHEN gdp < 1500 THEN 1 -- roughly this is the mid value for the dataset
	ELSE 0  
END) AS low_gdp_count,
ROUND(AVG(CASE 
	WHEN gdp < 1500 THEN life_expectancy  -- roughly this is the mid value for the dataset
	ELSE NULL  
END), 2) AS low_gdp_life_expec
FROM worldlifeexpectancy
;

-- There are 1326 rows with the gdp above 1500 and 1612 row with the gdp below 1500.
-- The average life expectancy of the 'High' category is 74.2. For the 'Low' category, the average life expectancy is 64.7
-- This an indicator that there is a positive correlation between the gdp and life expectancy.

-- A similar calculation can be done with the other columns (like worldlifeexpectancy.bmi or worldlifeexpectancy.schooling) in the dataset and visualize it in a BI tool like Tableau.

SELECT status , ROUND(AVG(life_expectancy),2) AS avg_life_expec, COUNT(status) AS status_count
FROM worldlifeexpectancy
WHERE life_expectancy > 0
GROUP BY status
;

-- For 'Developed' countries, the avg life expectancy is 79.2. 512 row where used for calculating the avg
-- For 'Developing' countries, the avg life expectancy is 66.83. 2416 row where used for calculating the avg
-- I filtered out the instances where the life expectancy data is missing

SELECT status, COUNT(DISTINCT country) AS country_count, ROUND(AVG(life_expectancy),2) AS avg_life_expec 
FROM worldlifeexpectancy
GROUP BY status 
;

-- I see that there are 32 'Developed' countries in this dataset while the number of 'Developing' countries is 161.
-- This could cause a bias in the numbers I am avering in the above queries. 

SELECT country, ROUND(AVG(life_expectancy),2) AS avg_life_expec, ROUND(AVG(bmi),2) AS avg_bmi
FROM worldlifeexpectancy
GROUP BY country 
HAVING ROUND(AVG(life_expectancy),2) > 0
	AND ROUND(AVG(bmi),2) > 0
ORDER BY avg_bmi DESC
;


-- By slimming throught the output of the query above, one can see that a lower bmi is correlated with a lower life expectancy.
-- The relationship between life expectancy and bmi is nontrivial. Hence a visualization tool could help unravel more details on the bmi-life_expectancy relationship. 

-- The last thing I want to look at is the adult mortality.
-- It could be interesting to find how many people are dying each year in teach country and if that is correlated to the respective life expectancy.
-- 

SELECT country, "year" , life_expectancy , adult_mortality ,
SUM(adult_mortality) OVER( PARTITION BY country ORDER BY "year" ) AS rolling_tot_adult_mortality
FROM worldlifeexpectancy
WHERE country LIKE 'United%'
;

-- The behaviour of the adult mortality seems unclear. 
-- The total population of each contry is not included in the dataset. Including such information could unravel nontrivial correlations.
-- By looking at the number of adult mortality with respect to the total population of each country, one could identify if the recorded life expectancy is trending upwards or downwards.





