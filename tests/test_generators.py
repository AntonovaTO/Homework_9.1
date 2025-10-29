from typing import Any, Callable, Dict, Iterator, List

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


# Фикстуры для тестовых данных
@pytest.fixture
def sample_transactions() -> List[Dict[str, Any]]:
    """Фикстура с тестовыми транзакциями"""
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        }
    ]


@pytest.fixture
def empty_transactions() -> List[Dict[str, Any]]:
    """Фикстура с пустым списком транзакций"""
    return []


def test_filter_usd_currency(sample_transactions: List[Dict[str, Any]]) -> None:
    """Тест фильтрации USD транзакций"""
    usd_transactions = filter_by_currency(sample_transactions, "USD")
    result = list(usd_transactions)

    assert len(result) == 2
    assert all(
        transaction["operationAmount"]["currency"]["code"] == "USD"
        for transaction in result
    )
    assert result[0]["id"] == 939719570
    assert result[1]["id"] == 142264268


def test_filter_rub_currency(sample_transactions: List[Dict[str, Any]]) -> None:
    """Тест фильтрации RUB транзакций"""
    rub_transactions = filter_by_currency(sample_transactions, "RUB")
    result = list(rub_transactions)

    assert len(result) == 1
    assert result[0]["operationAmount"]["currency"]["code"] == "RUB"
    assert result[0]["id"] == 873106923


def test_filter_nonexistent_currency(sample_transactions: List[Dict[str, Any]]) -> None:
    """Тест фильтрации по несуществующей валюте"""
    eur_transactions = filter_by_currency(sample_transactions, "EUR")
    result = list(eur_transactions)

    assert len(result) == 0
    assert result == []


def test_empty_transactions_list(empty_transactions: List[Dict[str, Any]]) -> None:
    """Тест с пустым списком транзакций"""
    result_generator = filter_by_currency(empty_transactions, "USD")
    result = list(result_generator)

    assert len(result) == 0
    assert result == []


def test_transaction_descriptions_returns_correct_descriptions(sample_transactions: List[Dict[str, Any]]) -> None:
    """Тест возврата корректных описаний транзакций"""
    descriptions = transaction_descriptions(sample_transactions)
    result = list(descriptions)

    expected_descriptions = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет"
    ]
    assert result == expected_descriptions
    assert len(result) == 3


def test_transaction_descriptions_empty_list(empty_transactions: List[Dict[str, Any]]) -> None:
    """Тест с пустым списком транзакций"""
    descriptions = transaction_descriptions(empty_transactions)
    result = list(descriptions)

    assert len(result) == 0
    assert result == []


def test_transaction_descriptions_single_transaction() -> None:
    """Тест с одной транзакцией"""
    single_transaction = [{
        "id": 123,
        "state": "EXECUTED",
        "date": "2023-01-01T00:00:00.000000",
        "operationAmount": {
            "amount": "100.00",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Одиночная операция",
        "from": "Счет 123",
        "to": "Счет 456"
    }]

    descriptions = transaction_descriptions(single_transaction)
    result = list(descriptions)

    assert len(result) == 1
    assert result[0] == "Одиночная операция"


@pytest.fixture
def card_generator() -> Callable[[int, int], Iterator[str]]:
    """Фикстура для создания генератора карт"""
    def _generator(start: int, end: int) -> Iterator[str]:
        return card_number_generator(start, end)
    return _generator


def test_card_number_generator_basic_range(card_generator: Callable[[int, int], Iterator[str]]) -> None:
    """Тест проверки создания номеров карт"""
    generator = card_generator(1, 5)
    result = list(generator)

    expected = [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005"
    ]
    assert result == expected
    assert len(result) == 5


def test_card_number_generator_single_number(card_generator: Callable[[int, int], Iterator[str]]) -> None:
    """Тест генератора с одним номером"""
    generator = card_generator(1, 1)
    result = list(generator)

    assert result == ["0000 0000 0000 0001"]
    assert len(result) == 1


def test_card_number_generator_large_numbers(card_generator: Callable[[int, int], Iterator[str]]) -> None:
    """Тест генератора с большими числами"""
    generator = card_generator(9999999999999998, 9999999999999999)
    result = list(generator)

    expected = [
        "9999 9999 9999 9998",
        "9999 9999 9999 9999"
    ]
    assert result == expected
