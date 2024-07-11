import csv
import pandas as pd


def reader_file_transaction_csv(file: str) -> list[dict]:
    """Функция считывающая csv файл и возвращающая список словарей"""
    with open(file, "r", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=";")
        header = next(reader)
        result = []
        for row in reader:
            row_dict = {
                "id": row[header.index("id")],
                "state": row[header.index("state")],
                "date": row[header.index("date")],
                "operationAmount": {
                    "amount": row[header.index("amount")],
                    "currecy": {
                        "name": row[header.index("currency_name")],
                        "code": row[header.index("currency_code")],
                    }
                },
                "description": row[header.index("description")],
                "from": row[header.index("from")],
                "to": row[header.index("to")]
            }
            result.append(row_dict)

    return result


if __name__ == "__main__":
    result = reader_file_transaction_csv("..\\data\\transactions.csv")
    print(result)
