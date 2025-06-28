'''
CREATE INDEX customers_id_idx
ON orders(customer_id);
'''

'''
CREATE INDEX order_id_price_idx
ON order_items(order_id, price);
'''

'''
CREATE INDEX product_name_idx
ON order_items(product_name); -> дропнут
'''