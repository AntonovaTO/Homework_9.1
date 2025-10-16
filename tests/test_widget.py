import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "input_string, expected",
    [
        ("Visa 1234567812345678", "Visa 1234 56** **** 5678"),
        ("MasterCard 1111222233334444", "MasterCard 1111 22** **** 4444"),
        ("Счет 12345678901234567890", "Счет **7890"),
    ],
)
def test_mask_account_card_valid(input_string: str, expected: str) -> None:
    """Тестирование корректных входных данных"""
    result = mask_account_card(input_string)
    assert result == expected


@pytest.mark.parametrize(
    "invalid_input",
    [
        "Card",
        "1234567812345678",
        "Unknown 1234567812345678",
    ],
)
def test_mask_account_card_invalid(invalid_input: str) -> None:
    """Тестирование некорректных входных данных"""
    result = mask_account_card(invalid_input)
    assert isinstance(result, str)


@pytest.mark.parametrize(
    "input_date, expected",
    [
        ("2023-07-15T10:30:00", "15.07.2023"),
        ("2022-12-31T23:59:59", "31.12.2022"),
        ("2019-07-03T18:35:29.512364", "03.07.2019"),
    ],
)
def test_get_date_valid(input_date: str, expected: str) -> None:
    """Тестирование правильности преобразования даты"""
    result = get_date(input_date)
    assert result == expected


@pytest.mark.parametrize(
    "invalid_date",
    [
        "2023-13-45T25:61:61",
        "not-a-date",
        "",
    ],
)
def test_get_date_invalid(invalid_date: str) -> None:
    """Тестирование нестандартных строк с датами"""
    result = get_date(invalid_date)
    assert isinstance(result, str)
