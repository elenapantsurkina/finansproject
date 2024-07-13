import csv
import pandas as pd
import json


# def reader_file_transaction_csv(file: str) -> list[dict]:
#     """Функция считывающая cvs файл и возвращающая список словарей"""
#     my_dict = reader_file_transaction_excel("..\\data\\transactions_excel.xlsx")
#
#     j = json.dumps(my_dict, indent=4, ensure_ascii=False)
#     with open("..\\result.json", "w") as f:
#         print(j, file=f)
def reader_file_transaction_excel(file: str) -> list[dict]:
    """Функция считывающая файл в формате excel и возвращающая список словарей"""
    df = pd.read_excel(file)  # читаем из экселя в DataFrame
    result = []
    rows_count = len(df)  # Получение количества строк в DataFrame
    for i in range(0, rows_count):
        row_dict = {
            "id": df.at[i, "id"],
            "state": df.at[i, "state"],
            "date": df.at[i, "date"],
            "operationAmount": {
                "amount": df.at[i, "amount"],
                "currency": {
                    "name": df.at[i, "currency_name"],
                    "code": df.at[i, "currency_code"],
                },
            },
            "description": df.at[i, "description"],
            "from": df.at[i, "from"],
            "to": df.at[i, "to"],
        }
        result.append(row_dict)
    return result


if __name__ == "__main__":
    result = reader_file_transaction_excel("..\\data\\transactions_excel.xlsx")
    print(result)
