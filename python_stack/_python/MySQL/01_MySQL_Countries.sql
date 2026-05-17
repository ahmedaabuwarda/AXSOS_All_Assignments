-- 1. What query would you run to get all the countries that speak Slovene? 
-- Your query should return the name of the country, language, and language percentage. 
-- Your query should arrange the result by language percentage in descending order. (1)
SELECT countries.name, languages.language , languages.percentage
FROM world.countries 
join world.languages on world.countries.id = world.languages.country_id 
where world.languages.language = 'Slovene'
order by world.languages.percentage DESC;

-- 2. What query would you run to display each country's total number of cities? 
-- Your query should return the name of the country and the total number of cities. 
-- Your query should arrange the result by the number of cities in descending order. (3)
select countries.name , count(cities.name) as cities_sum 
from countries 
join cities on countries.id = cities.country_id 
group by countries.name
order by cities_sum DESC;

-- 3. What query would you run to get all the cities in Mexico with a population greater than 500,000? 
-- Your query should arrange the results by population in descending order. (1)
select cities.name, cities.population, cities.country_id from countries
join cities on countries.id = cities.country_id
where countries.name = "Mexico" and cities.population > 500000
order by cities.population DESC;

-- 4. What query would you run to get all languages in each country with a percentage greater than 89%? 
-- Your query should arrange the result by percentage in descending order. (1)
select countries.name, languages.language, languages.percentage from countries
join languages on countries.id = languages.country_id
where languages.percentage > 89
order by languages.percentage DESC;

-- 5. What query would you run to get all the countries with a Surface Area below 501 
-- and a Population greater than 100,000? (2)
select countries.name, countries.surface_area, countries.population from countries 
where countries.surface_area < 501 and countries.population > 100000;

-- 6. What query would you run to get countries with only 
-- a Constitutional Monarchy with a capital greater than 200 and
-- a life expectancy greater than 75 years? (1)
select countries.name, countries.government_form, countries.capital, countries.life_expectancy 
from countries
where countries.government_form = "Constitutional Monarchy" 
and countries.capital > 200 and countries.life_expectancy > 75;

-- 7. What query would you run to get all the cities of Argentina inside the Buenos Aires district 
-- and have a population greater than 500,000? 
-- The query should return the Country Name, City Name, District, and Population. (2)
select countries.name, cities.name, cities.district, cities.population from countries
join cities on countries.id = cities.country_id
where countries.name = "Argentina" and cities.district = "Buenos Aires" and cities.population > 500000;

-- 8. What query would you run to summarize the number of countries in each region? 
-- The query should display the region's name and the number of countries. 
-- Also, the query should arrange the result by the number of countries in descending order. (2)
select countries.region, count(countries.name) AS countries
from countries group by countries.region
order by countries DESC;