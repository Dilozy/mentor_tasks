from datetime import datetime

request_data = """
2025-05-21T17:11:10 Вход в систему
2025-05-21T17:11:12 Авторизация
2025-05-21T17:11:25 Заполнение формы
...
2025-05-21T17:15:14 Выход из системы
"""

timestamps = [datetime.fromisoformat(log.split()[0]).timestamp()
              for log in request_data.strip().split("\n") if log != "..."]
total = sum(timestamps[i + 1] - timestamps[i] for i in range(len(timestamps) - 1))
avg = total / (len(timestamps) - 1)
print(avg)