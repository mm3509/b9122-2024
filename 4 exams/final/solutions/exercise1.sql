SELECT city.Name AS city_name, country.Name as country_name FROM city LEFT JOIN country ON city.CountryCode = country.Code where country.Name LIKE "%land%" AND city.Population > 500000;
