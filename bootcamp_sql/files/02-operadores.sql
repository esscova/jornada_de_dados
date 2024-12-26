-- Exercicios operadores e funções

-- 1. Liste os produtos cujo preço (unit_price) esteja entre 10 e 20.
SELECT * FROM products WHERE unit_price BETWEEN 10 and 20;

-- 2. Filtre os pedidos (orders) realizados no ano de 1997.
SELECT * FROM orders;
SELECT * FROM orders WHERE EXTRACT(YEAR FROM order_date) = 1997;

-- 3. Exiba o nome dos produtos e a quantidade em estoque (Units_in_stock) ordenados do maior para o menor.
SELECT product_name, units_in_stock FROM products ORDER BY units_in_stock DESC;

-- 4. Encontre os clientes cujo nome da empresa (company_name) começa com a letra "B".
SELECT * FROM customers WHERE company_name LIKE 'B%';