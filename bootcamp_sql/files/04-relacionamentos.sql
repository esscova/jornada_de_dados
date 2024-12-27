-- Exercicios: relacionamentos

-- 1. Liste os nomes dos produtos (ProductName) e os nomes de seus respectivos fornecedores (CompanyName).
-- tabelas: products e suppliers

SELECT 
	products.product_name,
	suppliers.company_name
FROM 
	products
	INNER JOIN suppliers ON products.supplier_id = suppliers.supplier_id
	;

-- 2. Mostre os detalhes dos pedidos (OrderID, OrderDate, ProductName, Quantity).
-- tabelas: orders, order_details e products

SELECT 
	orders.order_id, 
	orders.order_date, 
	products.product_name,
	order_details.quantity
FROM 
	orders
	JOIN order_details ON orders.order_id = order_details.order_id
	JOIN products ON order_details.product_id = products.product_id
	;
	
-- 3. Liste os nomes dos clientes (CompanyName) e os nomes dos funcionários (FirstName, LastName) responsáveis por seus pedidos.
-- Tabelas: Customers, Orders, Employees.

select * from orders;

SELECT
	customers.company_name,
	employees.first_name,
	employees.last_name
FROM
	customers
	JOIN orders ON customers.customer_id = orders.customer_id
	JOIN employees ON orders.employee_id = employees.employee_id
	;
