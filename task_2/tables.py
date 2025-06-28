'''CREATE TABLE customers
(
	id SERIAL PRIMARY KEY,
	name VARCHAR(40),
	email VARCHAR(256) UNIQUE
);'''

'''
CREATE TABLE orders
(
	id SERIAL PRIMARY KEY,
	customer_id INT,
	order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY (customer_id) REFERENCES customers(id)
);
'''

'''
CREATE TABLE order_items
(
	id SERIAL PRIMARY KEY,
	order_id INT,
	product_name VARCHAR(256),
	quantity INT DEFAULT 1,
	price NUMERIC(10, 2),
	FOREIGN KEY(order_id) REFERENCES orders(id)
);
'''