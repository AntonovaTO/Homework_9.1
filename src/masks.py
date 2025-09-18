import os

base_path = os.path.dirname(os.path.abspath(__file__))
full_path = os.path.join(base_path, "src", "masks")


def get_mask_card_number(card_number: str) -> str:
    """Функция для возврата маски номера карты по правилу: XXXX XX** **** XXXX"""
    if not isinstance(card_number, str):
        return "Ошибка: Номер карты должен быть строкой"

    cleaned_number = ""
    for char in card_number:
        if char.isdigit():
            cleaned_number += char

    if len(cleaned_number) != 16:
        return "Ошибка: Номер карты должен содержать 16 цифр"

    masked_number = f"{cleaned_number[:4]} " f"{cleaned_number[4:6]}** " f"**** " f"{cleaned_number[-4:]}"

    return masked_number


def get_mask_account(account_number: str) -> str:
    """Функция для возврата маски номера счета по правилу: **XXXX"""
    if not isinstance(account_number, str):
        return "Ошибка: Номер счета должен быть строкой"

    cleaned_number = ""
    for char in account_number:
        if char.isdigit():
            cleaned_number += char

    if len(cleaned_number) < 4:
        return "Ошибка: Номер счета должен содержать минимум 4 цифры"

    masked_number = f"**{cleaned_number[-4:]}"

    return masked_number


if __name__ == "__main__":
    # Правильные примеры
    print(get_mask_card_number("7000792289606361"))  # 7000 79** **** 6361
    print(get_mask_account("73654108430135874305"))  # **4305

    """Строка"""

