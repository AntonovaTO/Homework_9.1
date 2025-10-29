import pytest
from src.decorators import log


def test_decorator_direct_usage(capsys):
    """Тест прямого использования декоратора (без @ синтаксиса)"""

    # Создаем функцию без декоратора
    def plain_function(x: int, y: int) -> int:
        return x + y

    # Применяем декоратор напрямую
    decorated_func = log()(plain_function)

    # Вызываем декорированную функцию
    result = decorated_func(5, 3)
    assert result == 8

    captured = capsys.readouterr()
    assert "plain_function ok" in captured.out


def test_decorator_with_filename_direct():
    """Тест прямого использования декоратора с filename"""

    def file_function(x: int) -> int:
        return x * 10

    # Применяем декоратор с filename напрямую
    decorated_func = log(filename="direct_log.txt")(file_function)

    result = decorated_func(7)
    assert result == 70

    # Проверяем запись в файл
    with open("direct_log.txt", 'r', encoding='utf-8') as f:
        content = f.read()
        assert "file_function ok" in content


def test_decorator_direct_with_error(capsys):
    """Тест использования декоратора с ошибкой"""

    def error_function() -> float:
        return 10 / 0

    # Применяем декоратор напрямую
    decorated_func = log()(error_function)

    result = decorated_func()
    assert result is None

    captured = capsys.readouterr()
    assert "error_function error: ZeroDivisionError" in captured.out