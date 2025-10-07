from typing import Any, Dict, List

import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def transactions() -> List[Dict[str, Any]]:
    """Список словарей с транзакциями разных статусов"""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-07-15"},
        {"id": 2, "state": "CANCELED", "date": "2023-07-14"},
        {"id": 3, "state": "EXECUTED", "date": "2023-07-13"},
    ]


@pytest.fixture
def unsorted_transactions() -> List[Dict[str, Any]]:
    """Список словарей с транзакциями в разном порядке дат"""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-03-15"},
        {"id": 2, "state": "EXECUTED", "date": "2023-03-10"},
        {"id": 3, "state": "CANCELED", "date": "2023-03-20"},
    ]


def test_filter_by_state_executed(transactions: List[Dict[str, Any]]) -> None:
    """Тестирует фильтрацию транзакций по статусу EXECUTED"""
    result: List[Dict[str, Any]] = filter_by_state(transactions, "EXECUTED")
    assert len(result) == 2
    assert all(item["state"] == "EXECUTED" for item in result)


def test_filter_by_state_canceled(transactions: List[Dict[str, Any]]) -> None:
    """Тестирует фильтрацию транзакций по статусу CANCELED"""
    result: List[Dict[str, Any]] = filter_by_state(transactions, "CANCELED")
    assert len(result) == 1
    assert all(item["state"] == "CANCELED" for item in result)


def test_sort_by_date_desc(unsorted_transactions: List[Dict[str, Any]]) -> None:
    """Тестирует сортировку транзакций по дате в порядке убывания"""
    result: List[Dict[str, Any]] = sort_by_date(unsorted_transactions)
    assert result[0]["date"] == "2023-03-20"
    assert result[-1]["date"] == "2023-03-10"


def test_sort_by_date_asc(unsorted_transactions: List[Dict[str, Any]]) -> None:
    """Тестирует сортировку транзакций по дате в порядке возрастания"""
    result: List[Dict[str, Any]] = sort_by_date(unsorted_transactions, reverse=False)
    assert result[0]["date"] == "2023-03-10"
    assert result[-1]["date"] == "2023-03-20"
