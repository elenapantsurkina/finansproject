from typing import Any

import mask


def mask_account_card(number_account_card: str) -> Any:
    """Функция маскирующая счета и карты"""
    if "Счет " in number_account_card:
        number_accound = number_account_card[-20:]
        return number_accound + mask.get_mask_account(number_accound)
    else:
        number_card = "".join(number_account_card[-16:].split())
        return number_account_card[:-16] + mask.get_mask_card_number(number_card)



print(mask_account_card("Maestro 1596837868705199"))