'''
SELECT orders.id, orders.order_date
FROM orders JOIN customers ON customers.id = customer_id
WHERE customers.name = 'Иван Иванов'
'''

'''
SELECT product_name, quantity, price
FROM orders JOIN order_items
ON orders.id = order_items.order_id
WHERE orders.id = 1
ORDER BY order_items.price DESC
'''

'''
SELECT customers.name, SUM(order_items.price * order_items.quantity) as total_spent    
FROM orders JOIN order_items ON orders.id = order_items.order_id
			JOIN customers ON orders.customer_id = customers.id
GROUP BY customers.name
HAVING SUM(order_items.price * order_items.quantity) > 5000
ORDER BY total_spent DESC;
'''