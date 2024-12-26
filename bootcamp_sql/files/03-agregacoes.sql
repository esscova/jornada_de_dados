-- Exercicios agregacoes e funcoes de grupo

-- 1. Conte quantos produtos estão cadastrados na tabela Products.
SELECT COUNT(*) FROM products;

-- 2. Qual é o preço médio (unit_price) dos produtos?
SELECT AVG(unit_price) FROM products;

-- 3. Liste o total de pedidos realizados por cada cliente.
SELECT Customer_id,COUNT(Customer_id) FROM orders GROUP BY Customer_id;

-- 4. Qual é o maior pedido (OrderID) feito por cada funcionário (EmployeeID)?
SELECT employee_id,MAX(order_id) FROM orders GROUP BY employee_id;
