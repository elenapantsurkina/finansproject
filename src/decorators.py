from typing import Any
from typing import Callable
from functools import wraps


def log(filename: Any = None) -> Callable:
    """декоратор,который логирует вызов функции и ее результат в файл или в консоль"""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"my_function ok")
                else:
                    print(f"my_function ok")
            except Exception as e:
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"my_function error: {e}. Inputs: {args}, {kwargs} \n")
                else:
                    print(f"my_function error: {e}. Inputs: {args}, {kwargs} \n")
                    raise
            return result

        return wrapper

    return decorator


@log(filename="mylog.txt")
def my_function(x, y):
    return x/y


print(my_function(2, 1))
