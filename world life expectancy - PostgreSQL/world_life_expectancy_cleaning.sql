-- World Life Expectancy (Data Cleaning)
-- To maintain clarity, the exploratory data analysis will be performed in a different script.

SELECT *
FROM worldlifeexpectancy
;


-- Initial remarks: there are some missing data in the columns 'status' and 'Life expentacy'. This will be addressed at a later stage. 
-- First, I want to identify and remove duplicates.

-- Check that for each contry we do not have duplicate rows for the same year.

SELECT country, "year", CONCAT(country, "year"), COUNT(CONCAT(country, "year")) AS duplicate_count
FROM worldlifeexpectancy
GROUP BY country, "year", CONCAT(country, "year")
HAVING COUNT(CONCAT(country, "year")) > 1;

-- I see that there are 3 duplicates: (Ireland 2022), (Zimbabwe, 2019), (Senegal, 2009).
-- I need to identify the Roaw_ID of the duplicate items and then remove them.


SELECT *
FROM (
	SELECT row_id,
	CONCAT(country, "year"),
	ROW_NUMBER() OVER ( PARTITION BY CONCAT(country, "year") ORDER BY CONCAT(country, "year")) AS Row_Num
	FROM worldlifeexpectancy
	) AS Row_Table
WHERE Row_Num > 1
;

-- Now I need to delete the rows with the Raw_IDs that I identified with the query above.
-- Before deleting any items from the main table, I created a backup copy.

DELETE FROM worldlifeexpectancy 
WHERE row_id IN (
	SELECT row_id
FROM (
	SELECT row_id,
	CONCAT(country, "year"),
	ROW_NUMBER() OVER ( PARTITION BY CONCAT(country, "year") ORDER BY CONCAT(country, "year")) AS Row_Num
	FROM worldlifeexpectancy
	) AS Row_Table
WHERE Row_Num > 1
)
;


-- Sanity check: Now I need to double check that the duplicate rows were successfully deleted from the main table

SELECT *
FROM (
	SELECT row_id,
	CONCAT(country, "year"),
	ROW_NUMBER() OVER ( PARTITION BY CONCAT(country, "year") ORDER BY CONCAT(country, "year")) AS Row_Num
	FROM worldlifeexpectancy
	) AS Row_Table
WHERE Row_Num > 1
;

-- Sanity check 2: Now I run the query above on the backup table 

SELECT *
FROM (
	SELECT row_id,
	CONCAT(country, "year"),
	ROW_NUMBER() OVER ( PARTITION BY CONCAT(country, "year") ORDER BY CONCAT(country, "year")) AS Row_Num
	FROM worldlifeexpectancy_backup
	) AS Row_Table
WHERE Row_Num > 1
;

-- All good!

-- I have noticed that some rows have missing values in the 'status' column. I want to see those rows. 

SELECT *
FROM worldlifeexpectancy
WHERE status = ''
;

-- Now I want to check if I can fill those missing values

SELECT DISTINCT(country)
FROM worldlifeexpectancy
WHERE status = ''
;

-- I can see that there are only two values for status: "Developed" and "Developing"

-- Now I want to see the countries which have the status 'Developing'

SELECT DISTINCT(country)
FROM worldlifeexpectancy
WHERE status = 'Developing'


-- Now I want to update the status values for the countries listed with the query above with 'Developing'. If any rows have banck values, they should be repopulated. 

UPDATE worldlifeexpectancy
SET status = 'Developing'
WHERE country IN (
	SELECT DISTINCT(country)
	FROM worldlifeexpectancy
	WHERE status = 'Developing'
);


-- Now I want to do the same as above but for the developed countries

UPDATE worldlifeexpectancy
SET status = 'Developed'
WHERE country IN (
	SELECT DISTINCT(country)
	FROM worldlifeexpectancy
	WHERE status = 'Developed'
);

-- Done!
-- Sanity check 3: see if the table has any rows where the status is still unpopulated.

SELECT *
FROM worldlifeexpectancy
WHERE status <> 'Developed'
AND status <> 'Developing';

SELECT *
FROM worldlifeexpectancy_backup
WHERE status <> 'Developed'
AND status <> 'Developing';


-- I want to see if there are any NULL values in the status column

SELECT *
FROM worldlifeexpectancy
WHERE status IS NULL;

-- None found!

-- Now let us focus on the 'life_expectancy' column

SELECT *
FROM worldlifeexpectancy
WHERE life_expectancy IS NULL;

-- It looks like there are two rows with NULL values. One corresponds to Afganistan while the second corresponds to Albania. Both correspond to 2018.
-- For demonstrating purposes, let us assume that the missing value, for each country, should be close enough to the average of the life expectancy of 2017 and 2019.
-- This is an inaccurate approach but in a real situation, one might have a missing value from the database while knowing the exact value that should be there.
-- A similar peice of code should fix the issue. 

-- First I define a set of conditions to identify the targeted rows and to estimate the averages.
 
SELECT t1.country, t1.year, t1.life_expectancy,
t2.country, t2.year, t2.life_expectancy ,
t3.country, t3.year, t3.life_expectancy ,
round((t2.life_expectancy::numeric + t3.life_expectancy::numeric)/2 ,2) AS average
FROM worldlifeexpectancy t1, worldlifeexpectancy t2, worldlifeexpectancy t3
WHERE t1.life_expectancy IS NULL 
AND t1.country = t2.country
AND t1.country = t3.country
AND t1."year"  = t2."year" - 1 
AND t1."year" = t3."year" + 1
;


-- Now I need to feed the calculated averages into the empty slots in the life_expectancy column.

UPDATE worldlifeexpectancy t1
SET life_expectancy = round((
							t2.life_expectancy::NUMERIC
							+ 
							t3.life_expectancy::numeric)/2 ,1)
FROM worldlifeexpectancy t2, worldlifeexpectancy t3
WHERE t1.life_expectancy IS NULL 
AND t1.country = t2.country
AND t1.country = t3. country
AND t1."year"  = t2."year" - 1 
AND t1."year" = t3."year" + 1

;

-- Sanity check 4: I want to see if the calculated values have been injected into the database properly.

SELECT country, "year", life_expectancy 
FROM worldlifeexpectancy
WHERE country = 'Afghanistan'
OR country = 'Albania'


SELECT *
FROM worldlifeexpectancy
WHERE life_expectancy IS NULL 
;


-- Done!

