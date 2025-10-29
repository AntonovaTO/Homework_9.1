from typing import Any, Callable, Optional, TypeVar, cast

# Тип для возвращаемого значения декорируемой функции
T = TypeVar('T')


def log(filename: Optional[str] = None) -> Callable[[Callable[..., T]], Callable[..., T]]:
    """
    Декоратор для логирования выполнения функций.

    Args:
        filename: Имя файла для записи логов. Если None, логи выводятся в консоль.

    Returns:
        Декорированную функцию с логированием.
    """

    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        def wrapper(*args: Any, **kwargs: Any) -> Optional[T]:
            func_name = func.__name__
            inputs = f"Inputs: {args}, {kwargs}"

            try:
                # Выполняем функцию
                result: Optional[T] = func(*args, **kwargs)
                log_message = f"{func_name} ok\n"

            except Exception as e:
                log_message = f"{func_name} error: {type(e).__name__}. {inputs}\n"
                result = None

            # Записываем лог в файл или консоль
            if filename:
                with open(filename, 'a', encoding='utf-8') as f:
                    f.write(log_message)
            else:
                print(log_message, end='')

            return result

        return cast(Callable[..., T], wrapper)

    return decorator


# Пример использования
@log(filename="mylog.txt")
def my_function(x: int, y: int) -> int:
    return x + y


@log()  # Логи в консоль
def risky_function(a: int, b: int) -> float:
    return a / b


if __name__ == "__main__":  #pragma: no cover
    result1 = my_function(1, 2)  # Запишет в файл: "my_function ok"
    print(f"Result 1: {result1}")

    result2 = risky_function(10, 2)  # Выведет в консоль: "risky_function ok"
    print(f"Result 2: {result2}")

    result3 = risky_function(10, 0)  # Выведет в консоль: "risky_function error:
    print(f"Result 3: {result3}")  # ZeroDivisionError. Inputs: (10, 0), {}"
