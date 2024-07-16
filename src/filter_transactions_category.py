import json
from collections import Counter


def get_filter_transaction_category(transactions: list[dict]) -> dict:
    """Функция, принимвющая список словарей с данными о банковских операциях и строку поиска,
    и возвращающая список словарей, у которых в описании есть данная строка"""
    category = []
    for transaction in transactions:
        category.append(transaction.get("description"))
        counter_category = Counter(category)
    return counter_category


if __name__ == "__main__":
    with open("..\\data\\operations.json", encoding="UTF-8") as f:
        transactions = json.load(f)
        counter_category = get_filter_transaction_category(transactions)
        print(counter_category)
