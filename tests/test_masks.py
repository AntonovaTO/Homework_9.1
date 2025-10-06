import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.fixture
def mask_card_number() -> str:
    """Фикстура для функции get_mask_card_number"""
    return "7000792289606361"


def test_mask_card_number(mask_card_number: str) -> None:
    """Тест функции get_mask_card_number на маскировку номеров карт"""
    assert get_mask_card_number(mask_card_number) == "7000 79** **** 6361"


@pytest.fixture
def input_len_card_number() -> str:
    """Фикстура для ошибки количества символов"""
    return "706361"


def test_input_len_card_number(input_len_card_number: str) -> None:
    """Тест функции get_mask_card_number на ошибку количества символов"""
    assert get_mask_card_number(input_len_card_number) == "Ошибка: Номер карты должен содержать 16 цифр"


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("73654108430135874305", "**4305"),
        ("1234", "**1234"),  # минимальная длина
        ("1234567890", "**7890"),  # 10 цифр
    ],
)
def test_get_mask_account_number(account_number: str, expected: str) -> None:
    """Тест функции get_mask_account на маскировку номеров счетов"""
    result = get_mask_account(account_number)
    assert result == expected


@pytest.fixture
def input_len_account_number() -> str:
    """Фикстура для ошибки количества символов"""
    return "736"


def test_input_len_account_number(input_len_account_number: str) -> None:
    """Тест функции get_mask_account на ошибку количества символов"""
    assert get_mask_account(input_len_account_number) == "Ошибка: Номер счета должен содержать минимум 4 цифры"
