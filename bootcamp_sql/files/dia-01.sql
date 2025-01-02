-- 1. Como você exibiria todos os registros de uma tabela chamada "customers"?
SELECT * FROM customers;

-- Se você quisesse selecionar apenas o nome de contato e a cidade dos clientes na tabela "customers", como faria isso?
SELECT 
	contact_name,
	city
FROM
	customers;

-- 3. Como você listaria todos os países registrados na tabela "customers"?
SELECT country FROM customers;

-- 4. Se você quiser listar apenas os países distintos, ou seja, sem repetições, como faria essa consulta na tabela "customers"?
SELECT
	DISTINCT (country)
FROM
	customers;

-- 5. Como você contaria quantos países únicos existem na tabela "customers"?
SELECT
	COUNT(DISTINCT(country))
FROM 
	customers;

-- 6. Como você selecionaria todos os clientes que estão no México na tabela "customers"?
SELECT * FROM customers WHERE country = 'Mexico';

-- 7. Se você souber o ID de um cliente, como poderia buscar esse cliente na tabela "customers"?
SELECT 
	*
FROM
	customers
WHERE
	customer_id = 'PERIC';

-- 8. Como você usaria a cláusula AND para filtrar registros, por exemplo, para selecionar clientes do país "Germany" e da cidade "Berlin"?
SELECT *
FROM customers
WHERE 
	country = 'Germany' AND city = 'Berlin';

-- 9. Como você filtraria clientes que estão em várias cidades, como "Berlin" ou "Aachen", usando a cláusula OR?
SELECT *
FROM customers
WHERE 
	city = 'Berlin' OR city = 'Aachen';

-- 10. Se você quiser excluir os clientes da Alemanha da sua consulta, qual seria a sintaxe na cláusula WHERE?
SELECT *
FROM customers
WHERE country <> 'Germany';

-- 11. Como você pode combinar AND, OR e NOT para selecionar clientes da Alemanha ou da cidade de "Aachen"?
SELECT *
FROM customers
WHERE 
	country = 'Germany' AND (city = 'Berlin' OR city = 'Aachen');

-- 12. Como você excluiria clientes tanto da Alemanha quanto dos Estados Unidos da sua consulta?
SELECT *
FROM customers
WHERE 
	country <> 'Germany' AND country <> 'USA';

-- 13. Se você quiser ordenar os registros de clientes por país, como você faria isso na consulta SQL?
SELECT
	company_name,
	country
FROM 
	customers
ORDER BY 
	country;

-- 14. Como você ordenaria os clientes por país em ordem descendente?
SELECT 
	company_name,
	country
FROM
	customers
ORDER BY
	country DESC;

-- 15. Como você ordenaria os clientes primeiro pelo país e depois pelo nome do contato?
SELECT
	company_name,
	country
FROM
	customers
ORDER BY
	country,
	company_name;

-- 16. E se você quisesse ordenar os registros de clientes pelo país em ordem ascendente e pelo nome de contato em ordem descendente, como faria isso?
SELECT
	contact_name,
	country
FROM
	customers
ORDER BY
	country ASC,
	contact_name DESC;

-- 17. Como você selecionaria clientes cujo nome de contato começa com a letra "A"?
SELECT contact_name
FROM customers
WHERE contact_name LIKE 'A%';

-- 18. Como você filtraria clientes cujo nome de contato não começa com a letra "A"?
SELECT contact_name
FROM customers
WHERE contact_name NOT LIKE 'A%';

-- 19. Como você selecionaria clientes de países específicos, como Alemanha, França e Reino Unido?
SELECT *
FROM customers
WHERE country IN ('Germany', 'France', 'UK')

-- 20. Se você quiser excluir clientes de alguns países específicos, como Alemanha, França e Reino Unido, como faria isso na consulta?
SELECT *
FROM customers
WHERE country NOT IN ('Germany', 'France', 'UK');