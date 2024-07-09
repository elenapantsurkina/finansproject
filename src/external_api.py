import requests
from dotenv import load_dotenv
import os

load_dotenv("..\\.env")


def get_transaction_sum_rub(transaction: dict) -> float:
    """функция, которая принимает на вход транзакцию и возвращает сумму транзакции"""
    amount = float(transaction["operationAmount"]["amount"])
    currency = transaction["operationAmount"]["currency"]["code"]
    if currency == "RUB":
        return amount
    else:
        API_KEY = os.environ.get("API_KEY")
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
        headers = {"apikey": API_KEY}
        response = requests.get(url, headers=headers)
        status_code = response.status_code
        if status_code != 200:
            print(f"Запрос не был успешным. Возможная причина: {response.reason}")

        else:
            result = response.json()
            return result["result"]


if __name__ == "__main__":
    transaction = {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    result = get_transaction_sum_rub(transaction)
    print(result)
