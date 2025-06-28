import os
import random
from datetime import datetime

import psycopg
from dotenv import load_dotenv
from faker import Faker


load_dotenv()


conn_params = {
    "dbname": "task_3",
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST")
}

fake = Faker('ru_RU')

def create_customers():
    """Создает 10 000 тестовых пользователей"""
    with psycopg.connect(**conn_params) as conn:
        with conn.cursor() as cur:
            print("Создание 10 000 пользователей...")
            batch = []
            for i in range(1, 10_001):
                name = fake.name()
                email = fake.unique.email()
                batch.append((name, email))
                
                if i % 1000 == 0:  # Вставка пачками по 1000
                    cur.executemany(
                        "INSERT INTO customers (name, email) VALUES (%s, %s)",
                        batch
                    )
                    conn.commit()
                    batch = []
                    print(f"Добавлено {i} пользователей")

def create_orders():
    """Создает 20 000 тестовых заказов"""
    with psycopg.connect(**conn_params) as conn:
        with conn.cursor() as cur:
            print("Создание 20 000 заказов...")
            
            # Получаем всех пользователей
            cur.execute("SELECT id FROM customers;")
            customer_ids = [row[0] for row in cur.fetchall()]
            
            batch = []
            for i in range(1, 20_001):
                customer_id = random.choice(customer_ids)
                order_date = fake.date_time_between(start_date='-1y', end_date='now')
                batch.append((customer_id, order_date))
                
                if i % 1000 == 0:  # Вставка пачками по 1000
                    cur.executemany(
                        "INSERT INTO orders (customer_id, order_date) VALUES (%s, %s)",
                        batch
                    )
                    conn.commit()
                    batch = []
                    print(f"Добавлено {i} заказов")

def insert_order_items():
    """Вставка 1 000 000 позиций заказов"""
    with psycopg.connect(**conn_params) as conn:
        with conn.cursor() as cur:
            # Получаем все order_id
            cur.execute("SELECT id FROM orders;")
            order_ids = [row[0] for row in cur.fetchall()]

            print("Начало вставки 1 000 000 позиций заказов...")
            start_time = datetime.now()
            
            # Создаем временную таблицу
            cur.execute("""
                CREATE TEMPORARY TABLE temp_order_items (
                    order_id INT,
                    product_name VARCHAR(256),
                    quantity INT,
                    price NUMERIC(10, 2)
                ) ON COMMIT DROP;
            """)
                
            # Используем COPY в текстовом формате (более надежный вариант)
            with cur.copy("""
                COPY temp_order_items (order_id, product_name, quantity, price) 
                FROM STDIN WITH (FORMAT text)
            """) as copy:
                for _ in range(1_000_000):
                    order_id = random.choice(order_ids)
                    product_num = random.randint(1, 500)
                    quantity = random.randint(1, 10)
                    price = round(random.uniform(100, 100_000), 2)
                    
                    # Формируем строку для COPY (значения разделены табуляцией)
                    row = f"{order_id}\tТовар {product_num}\t{quantity}\t{price}"
                    copy.write(row + "\n")
            
            # Копируем из временной таблицы в целевую
            cur.execute("""
                INSERT INTO order_items (order_id, product_name, quantity, price)
                SELECT order_id, product_name, quantity, price 
                FROM temp_order_items;
            """)
            
            conn.commit()
            
            duration = datetime.now() - start_time
            print(f"Вставка завершена за {duration.total_seconds():.2f} секунд")

if __name__ == "__main__":
    create_customers()
    create_orders()
    insert_order_items()
    
    print("Все данные успешно созданы!")