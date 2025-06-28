import os
import random
from datetime import datetime

import psycopg
from dotenv import load_dotenv


load_dotenv(dotenv_path="./.task_3.env")


conn_params = {
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST")
}

def generate_data():
    with psycopg.connect(**conn_params) as conn:
        with conn.cursor() as cur:
            # Получаем все существующие order_id
            cur.execute("SELECT id FROM orders;")
            order_ids = [row[0] for row in cur.fetchall()]

            if not order_ids:
                raise ValueError("В таблице orders нет записей!")

            for _ in range(1_000_000):
                order_id = random.choice(order_ids)
                product_num = random.randint(1, 500)
                quantity = random.randint(1, 10)
                price = round(random.uniform(100, 100_000), 2)
                
                yield (order_id, f"Товар {product_num}", quantity, price)

def insert_data():
    start_time = datetime.now()
    print(f"Начало вставки: {start_time}")
    
    with psycopg.connect(**conn_params) as conn:
        with conn.cursor() as cur:
            # Создаем временную таблицу для batch-вставки
            with conn.transaction():
                cur.execute("""
                CREATE TEMPORARY TABLE temp_order_items (
                    order_id INT,
                    product_name VARCHAR(256),
                    quantity INT,
                    price NUMERIC(10, 2)
                );
            """)

                # Копируем данные во временную таблицу
                with cur.copy("COPY temp_order_items FROM STDIN") as copy:
                    for record in generate_data():
                        copy.write_row(record)

                # Вставляем из временной таблицы в целевую
                cur.execute("""
                    INSERT INTO order_items (order_id, product_name, quantity, price)
                    SELECT order_id, product_name, quantity, price 
                    FROM temp_order_items;
                """)
    
    end_time = datetime.now()
    duration = end_time - start_time
    print(f"Вставка завершена за {duration.total_seconds():.2f} секунд")

if __name__ == "__main__":
    insert_data()