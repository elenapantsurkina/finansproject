import logging

logger = logging.getLogger("logs")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("..\\logs\\masks.log", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(number_cart: str) -> str:
    """Функция,маскирующая номер карты клиента"""
    logger.info("Маскируем карту клиента")
    return f"{number_cart[0:4]} {number_cart[4:6]}{'** ****'} {number_cart[-4:]}"


# print(get_mask_card_number(str(7000792289606361)))


def get_mask_account(number_account: str) -> str:
    """Функция, маскирующая номер счета клиента"""
    logger.info("Маскируем счет клиента")
    return f"{'**'}{number_account[-4:]}"


# print(get_mask_account(str(73654108430135874305)))
