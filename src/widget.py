from datetime import datetime
from typing import Any

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(number_account_card: str) -> Any:
    """Функция маскирующая счета и карты"""
    if "Счет " in number_account_card:
        number_accound = number_account_card[-20:]
        return number_accound + get_mask_account(number_accound)
    else:
        number_card = "".join(number_account_card[-16:].split())
        return number_account_card[:-16] + get_mask_card_number(number_card)


print(mask_account_card("Maestro 1596837868705199"))


def get_data(data: str) -> str:
    """Функция преобразования даты"""
    d = datetime.strptime(data, "%Y-%m-%dT%H:%M:%S.%f")
    return d.strftime("%d.%m.%Y")


print(get_data("2018-07-11T02:26:18.671407"))
