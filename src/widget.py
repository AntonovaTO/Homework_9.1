from src.masks import get_mask_account, get_mask_card_number
from datetime import datetime


def mask_account_card(card_number: str) -> (str, str):
    """Функция для маскировки номера карты/счета"""

    # Разделяем строку на части
    parts = card_number.split()

    # Если это счет (содержит слово "Счет")
    if "Счет" in parts:
        # Берем последнюю часть как номер счета
        account_number = parts[-1]
        masked_number = get_mask_account(account_number)
        return f"Счет {masked_number}"

    # Если это карта (Visa, Maestro, MasterCard, и т.п.)
    else:
        # Берем название карты (все части кроме последней)
        card_name = " ".join(parts[:-1])
        # Берем номер карты (последняя часть)
        card_num = parts[-1]
        masked_number = get_mask_card_number(card_num)
        return f"{card_name} {masked_number}"


def get_date(date_str: str) -> str:
    """Функция которая принимает на вход строку с датой в формате
    "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ" """
    try:
        return datetime.fromisoformat(date_str.replace('Z', '')).strftime('%d.%m.%Y')
    except ValueError:
        return date_str


if __name__ == "__main__":
    print(mask_account_card("Visa Platinum 7000792289606361"))  # Visa Platinum 7000 92** **** 6361
    print(mask_account_card("Maestro 7000792289606361"))       # Maestro 7000 92** **** 6361
    print(mask_account_card("Счет 73654108430135874305"))      # Счет **4305
    print(get_date("2024-03-11T02:26:18.671407"))              # "ДД.ММ.ГГГГ"