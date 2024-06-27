from typing import Any
from typing import Callable
from functools import wraps


def log(filename: Any = None) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            log_message = "my_function ok"
            result = func(*args, **kwargs)
            try:

                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(log_message)
                else:
                    print(log_message)
            except Exception as e:
                print(f"my_function error: {e}. Inputs: {args}, {kwargs}")
            return result

        return wrapper

    return decorator


@log(filename="mylog.txt")
def my_function(x, y):
    return x/y


print(my_function(2, 1))
