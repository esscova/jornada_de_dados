-- 1. **Selecione todos os clientes da tabela `customers`.**
SELECT *
FROM customers;

-- 2. **Selecione os nomes de contato e cidades de todos os clientes da tabela `customers`.**
SELECT 
	contact_name,
	city
FROM customers;

-- 3. **Selecione todos os países distintos da tabela `customers`.**
SELECT DISTINCT(country)
FROM customers;

-- 4. **Selecione todos os clientes que estão localizados no México.**
SELECT *
FROM customers
WHERE country = 'Mexico';

-- 5. **Selecione todos os clientes com um `customer_id` específico.**
SELECT *
FROM customers
WHERE customer_id = 'TORTU';

-- 6. **Selecione todos os clientes da Alemanha que estão na cidade de Berlim.**
SELECT *
FROM customers
WHERE 
	country = 'Germany' AND city = 'Berlin';

-- 7. **Selecione todos os clientes da cidade de Berlim ou Aachen.**
SELECT *
FROM customers
WHERE city IN ('Berlin', 'Aachen');

-- 8. **Selecione todos os clientes que não estão localizados na Alemanha.**
SELECT *
FROM customers
WHERE country NOT IN ('Germany');

-- 9. **Selecione todos os clientes que estão na Alemanha ou na cidade de Berlim ou Aachen.**
SELECT *
FROM customers
WHERE country = 'Germany'
AND city IN ('Berlin','Aachen');

-- 10. **Selecione todos os produtos com preço inferior a 20.**
SELECT *
FROM products
WHERE unit_price < 20;

-- 11. **Selecione todos os produtos com preço superior a 100.**
SELECT *
FROM products
WHERE unit_price > 100;

-- 12. **Selecione todos os produtos com preço menor ou igual a 50.**
SELECT *
FROM products
WHERE unit_price <= 50;

-- 13. **Selecione todos os produtos com quantidade em estoque maior ou igual a 10.**
SELECT *
FROM products
WHERE units_in_stock >= 10;

-- 14. **Selecione todos os produtos cujo preço não é 30.**
SELECT *
FROM products
WHERE unit_price <> 30;

-- 15. **Selecione todos os produtos com preço entre 50 e 100 (exclusive).**
SELECT *
FROM products
WHERE unit_price BETWEEN 50 AND 100;

-- 16. **Selecione todos os produtos com preço fora do intervalo entre 20 e 40.**
SELECT *
FROM products
WHERE unit_price NOT BETWEEN 20 AND 40;

-- 17. **Selecione todos os clientes cujo nome de contato é nulo.**
SELECT *
FROM customers
WHERE contact_name IS NULL;

-- 18. **Selecione todos os clientes cujo nome de contato não seja nulo.**
SELECT *
FROM customers
WHERE contact_name IS NOT NULL;

-- 19. **Selecione todos os clientes cujo nome de contato começa com a letra "a".**
SELECT *
FROM customers
WHERE contact_name LIKE 'a%';

-- 20. **Selecione todos os clientes cujo nome de contato termina com a letra "a".**
SELECT *
FROM customers
WHERE contact_name LIKE '%a';

-- 21. **Selecione todos os clientes cujo nome de contato contém "or".**
SELECT *
FROM customers
WHERE contact_name LIKE '%or%';

-- 22. **Selecione todos os clientes cujo nome de contato tem "r" na segunda posição.**
SELECT *
FROM customers 
WHERE contact_name LIKE '_r%';

-- 23. **Selecione todos os clientes cujo nome de contato começa com "A" e tem pelo menos 3 caracteres de comprimento.**
SELECT *
FROM customers
WHERE contact_name LIKE 'A_%_%';

-- 24. **Selecione todos os clientes cujo nome de contato começa com "A" e termina com "o".**
SELECT *
FROM customers
WHERE contact_name LIKE 'A%o';

-- 25. **Selecione todos os clientes cujo nome de contato NÃO começa com "a".**
SELECT *
FROM customers
WHERE contact_name NOT LIKE 'A%';