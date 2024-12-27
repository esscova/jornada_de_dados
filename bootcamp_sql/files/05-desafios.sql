-- DESAFIOS

-- Encontre o total de vendas (preço unitário x quantidade) para cada produto.
-- Tabelas: `OrderDetails`.

SELECT 
	product_id, 
	SUM(unit_price * quantity) AS total_vendas 
FROM 
	order_details
GROUP BY
	product_id;

-- Liste os cinco produtos mais vendidos (baseando-se na soma das quantidades vendidas).
-- Dica: Use `SUM` e `ORDER BY LIMIT`.

SELECT 
	product_id,
	SUM(quantity) AS quantidade_vendida
FROM
	order_details
GROUP BY
	product_id
ORDER BY quantidade_vendida DESC LIMIT 5;

-- Quais categorias (`CategoryName`) têm mais de 10 produtos cadastrados?
-- Tabelas: `Categories` e `Products`.

SELECT 
	categories.category_name
FROM
	categories
JOIN 
	products ON products.category_id = categories.category_id
GROUP BY
	categories.category_name
HAVING 
	COUNT(categories.category_name) > 10;

-- Identifique os três clientes que mais realizaram pedidos.
-- Tabelas: `Customers` e `Orders`.

SELECT 
	c.customer_id,
	COUNT(o.order_id) AS total_pedidos
FROM
	customers c
JOIN
	orders o ON o.customer_id = c.customer_id
GROUP BY
	c.customer_id
ORDER BY
	total_pedidos DESC
LIMIT 3;

-- Liste as cidades com mais de cinco fornecedores.
-- Tabelas: `Suppliers`.

SELECT 
	city, 
	country,
	COUNT(supplier_id) AS total_fornecedores
FROM
	suppliers
GROUP BY
	city,
	country
HAVING
	COUNT(supplier_id) > 5;