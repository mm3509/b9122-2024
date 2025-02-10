SELECT country.name FROM country LEFT JOIN city ON country.code = city.countryCode
WHERE city.countryCode IS NULL
