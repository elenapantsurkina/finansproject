def get_mask_card_number(number_cart: str) -> str:
    """Функция,маскирующая номер карты клиента"""
    return f"{number_cart[0:4]} {number_cart[4:6]}{'**  ****'} {number_cart[-4:]}"


print(get_mask_card_number(str(7000792289606361)))


def get_mask_account(number_account: str) -> str:
    """Функция, маскирующая номер счета клиента"""
    return f"{'**'}{number_account[-4:]}"


print(get_mask_account(str(73654108430135874305)))
