import json
from collections import Counter


def get_filter_transaction_category(transactions: list[dict], category_list: list) -> dict:
    """Функция, принимающая список словарей с данными о банковских операциях и список категорий операций,
    а возвращающая словарь, в котором ключи — это названия категорий,
     а значения — это количество операций в каждой категории."""
    category = []
    counter_category = {}
    for transaction in transactions:
        if transaction.get("description") in category_list:
            category.append(transaction.get("description"))
            counter_category = Counter(category)
    return counter_category


if __name__ == "__main__":
    with open("..\\data\\operations.json", encoding="UTF-8") as f:
        transactions = json.load(f)
        category_list = [
            "Перевод организации", "Перевод с карты на карту",
            "Открытие вклада","Перевод с карты на счет","Перевод со счета на счет"]
        counter_category = get_filter_transaction_category(transactions,category_list)
        print(counter_category)
