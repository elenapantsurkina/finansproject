import json


def get_transactions_list(my_file_path: str) -> list:
    """Функция принимающая путь до файла в формате json и возвращающая список словарей"""
    try:
        with open(my_file_path, "r", encoding="utf-8") as f:
            try:
                transactions_list_my = json.load(f)
                if transactions_list_my == []:
                    return []
            except json.JSONDecodeError:
                return []
    except FileNotFoundError:
        return []

    return transactions_list_my


if __name__ == "__main__":
    my_file_path = "..\\data\\operations.json"
    transactions_list_my = get_transactions_list(my_file_path)
    print(transactions_list_my)
