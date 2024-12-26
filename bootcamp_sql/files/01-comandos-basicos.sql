-- Exercicios comandos básicos

-- 1. Liste todos os produtos na tabela Products.
SELECT * FROM products;

-- 2. Mostre os nomes (product_name) e os preços (unit_price) dos produtos na tabela Products.
SELECT product_name, unit_price FROM products;

-- 3. Filtre os produtos cujo preço (unit_price) seja maior que 20.
SELECT * FROM products WHERE unit_price > 20;

-- 4. Liste os fornecedores (suppliers) que estão localizados no Reino Unido (UK).
SELECT * FROM suppliers;
SELECT * FROM suppliers WHERE country = 'UK';

-- 5. Mostre os clientes (customers) localizados na cidade de Londres (London).
SELECT * FROM customers;
SELECT * FROM customers WHERE city = 'London';