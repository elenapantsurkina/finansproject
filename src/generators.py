from typing import Generator


def transaction_descriptions(transactions: list) -> Generator:
    """Генератор, который принимает список словарей и возвращает описание каждой операции по очереди"""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, end: int) -> Generator:
    """Генератор номеров банковских карт"""
    for number in range(start, end):
        card_number = str(number)
        while len(card_number) < 16:
            card_number = "0" + card_number
        formatted_cart_number = f"{card_number[0:5]} {card_number[5:9]} {card_number[9:13]} {-4:}"
        yield formatted_cart_number


def filter_by_currency(transactions: list, currency: str) -> Generator:
    """Функция, которая принимает список словарей с банковскими операциями и возвращает итератор,
    который выдает по очереди операции, в которых указана заданная валюта"""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction
