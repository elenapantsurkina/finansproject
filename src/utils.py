import json
import logging


logger = logging.getLogger("logs")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("..\\logs\\utils.log", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_transactions_list(my_file_path: str) -> list:
    """Функция принимающая путь до файла в формате json и возвращающая список словарей"""
    try:
        logger.info("Указываем путь до файла")
        with open(my_file_path, "r", encoding="utf-8") as f:
            try:
                logger.info("Получаем список транзакций")
                transactions_list_my = json.load(f)
                if transactions_list_my == []:
                    return []
            except json.JSONDecodeError as ex:
                logger.error(f"Произошла ошибка: {ex}")

                return []
    except FileNotFoundError as ex:
        logger.error(f"Произошла ошибка: {ex}")
        return []

    return transactions_list_my


if __name__ == "__main__":
    my_file_path = "..\\data\\operations.json"
    transactions_list_my = get_transactions_list(my_file_path)
    print(transactions_list_my)
