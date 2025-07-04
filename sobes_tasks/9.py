import time
from functools import wraps


def retry(*, delay: int):
    def inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            times_retried = 0
            while True:
                try:
                    return func(*args, **kwargs)
                except Exception:
                    time.sleep(delay)
                    times_retried += 1
                    print(f"Error while executing the function, times retried {times_retried}")
        return wrapper
    return inner


@retry(delay=1)
def div_by_zero():
    return 1 / 0

print(div_by_zero())