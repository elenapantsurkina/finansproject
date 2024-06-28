from functools import wraps
from typing import Any, Callable


def log(filename: Any = None) -> Callable:
    """декоратор,который логирует вызов функции и ее результат в файл или в консоль"""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                log_messege = "my_function ok\n"

            except Exception as e:
                result = None
                log_messege = f"my_function error: {e}. Inputs: {args}, {kwargs} \n"
            if filename:
                with open(filename, "a", encoding="utf-8") as file:
                    file.write(log_messege)
            else:
                print(log_messege)
            return result

        return wrapper

    return decorator


@log(filename="mylog.txt")
def my_function(x, y):
    return x / y


my_function(2, 0)
