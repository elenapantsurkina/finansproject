import json
import re


def get_filter_transaction(transactions: list[dict], bank_op: str) -> list[dict]:
    """Функция, принимвющая список словарей с данными о банковских операциях и строку поиска,
    и возвращающая список словарей, у которых в описании есть данная строка"""
    list_bank_op = []
    for transaction in transactions:
        if "description" in transaction and re.search(bank_op, transaction["description"], flags=re.IGNORECASE):
            list_bank_op.append(transaction)
    return list_bank_op
    #     if transaction.get("description") == bank_op:
    #         list_bank_op.append(transaction)
    # return list_bank_op


if __name__ == "__main__":
    with open("..\\data\\operations.json", encoding="UTF-8") as f:
        transactions = json.load(f)
        list_bank_op = get_filter_transaction(transactions, "Перевод организации")
        print(list_bank_op)

    # bank_op = "Перевод организации"
    # transactions = [
    #     {
    #         "id": 441945886,
    #         "state": "EXECUTED",
    #         "date": "2019-08-26T10:50:58.294041",
    #         "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
    #         "description": "Перевод организации",
    #         "from": "Maestro 1596837868705199",
    #         "to": "Счет 64686473678894779589",
    #     },
    #     {
    #         "id": 41428829,
    #         "state": "EXECUTED",
    #         "date": "2019-07-03T18:35:29.512364",
    #         "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
    #         "description": "Перевод организации",
    #         "from": "MasterCard 7158300734726758",
    #         "to": "Счет 35383033474447895560",
    #     },
    #     {
    #         "id": 939719570,
    #         "state": "EXECUTED",
    #         "date": "2018-06-30T02:08:58.425572",
    #         "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
    #         "description": "Открытие вклада",
    #         "from": "Счет 75106830613657916952",
    #         "to": "Счет 11776614605963066702",
    #     },
    # ]
    # list_bank_op = get_filter_transaction(transactions, bank_op)
    # print(list_bank_op)
