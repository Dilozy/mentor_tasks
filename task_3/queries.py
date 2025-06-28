'''
EXPLAIN ANALYZE
SELECT order_items.product_name
FROM order_items
WHERE price > 10000 and order_id = 4
'''

'''
EXPLAIN ANALYZE
SELECT orders.id
FROM orders
WHERE customer_id = 1;
'''

'''
EXPLAIN ANALYZE
SELECT orders.id
FROM orders
WHERE customer_id > 20 -> индекс не работает
'''

'''
EXPLAIN ANALYZE
SELECT orders.id
FROM orders
WHERE customer_id > 20 AND customer_id < 30; -> выше селективность, индекс работает
'''

'''
--SELECT orders.id
--FROM orders
--WHERE customer_id = 30

BEGIN;

   WITH new_order AS (INSERT INTO orders(customer_id)
	   VALUES (30)
	   RETURNING id)    
    
    INSERT INTO order_items(order_id, product_name, quantity, price)
    SELECT 
        new_order.id,
        items.*
    FROM 
        new_order,
        (VALUES
            ('Ноутбук Huawei', 1, 89999.99),
            ('Беспроводная мышь', 2, 2499.50),
            ('Смартфон Samsung', 1, 65490.00),
            ('Наушники Sony', 2, 8990.00)
        ) AS items(product_name, quantity, price);
COMMIT;
'''


