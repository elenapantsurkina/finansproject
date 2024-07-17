import json
from src.utils import get_transactions_list
from src.reader_file import reader_file_transaction_csv, reader_file_transaction_excel
from src.processing import filter_by_state, sort_by_date
from src.filter_transactions import get_filter_transaction
from src.filter_transactions_category import get_filter_transaction_category
from src.widget import mask_account_card


def main():
    while True:
        print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n"
              "Выберите необходимый пункт меню:\n"
              "1. Получить информацию о транзакциях из JSON-файла\n"
              "2. Получить информацию о транзакциях из CSV-файла\n"
              "3. Получить информацию о транзакциях из XLSX-файла")
        user_input = input()
        if user_input not in ["1", "2", "3"]:
            print("Вами не выбран доступный формат файла")
            break
        elif user_input == "1":
            print("Для обработки выбран JSON-файл")
            # continue
            transactions = get_transactions_list("..\\data\\operations.json")
        elif user_input == "2":
            print("Для обработки выбран CSV-файл")
            # continue
            transactions = reader_file_transaction_csv("..\\data\\transactions.csv")
        elif user_input == "3":
            print("Для обработки выбран XLCX-файл")
            # continue
            transactions = reader_file_transaction_excel("..\\data\\transactions_excel.xlsx")
        input_user_state = input("Введите статус, по которому необходимо выполнить фильтрацию.\n "
                  "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING").upper()
        if not in ["EXECUTED", "CANCELED", "PENDING"]:
            print(f"Статус операции {input_user_state} не доступен.")
            break
        else:
            print(f"Операции отфильтрованы по статусу{input_user_state}")
            filtered_transactions = filter_by_state(transactions, input_user_state)
            user_input_data = input("Отсортировать операции по дате? Да/Нет").upper()
                if user_input == "Да":
                    input_user_sort = input("Отсортировать по возрастанию/по убыванию").upper()
                else:
                    input_user_sort = input("Отсортировать по возрастанию/по убыванию").upper()
                        if input_user_sort == "по возрастанию"
                            filtered_transactions = sort_by_date(filtered_transactions)
                        else:
                            pass
                            input_user_rub = input("Выводить только рублевые тразакции? Да/Нет").upper()

                            if input_user_rub == "Да":
                            filtered_transactions = filtered_transactions["operationAmount"]["amount"]["currency"]
                        else:
                            pass
                        input_user_filter_description = input(
                            "Отфильтровать список транзакций по определенному слову в описании? Да/Нет").upper()
                        if input_user_filter_description == "Да":
                            input_user_filter_description = input("Введите категорию фильтрации: ").upper()
                            filtered_transactions = get_filter_transaction(filtered_transactions,
                                                                           bank_op=input_user_filter_description)
                        elif:
                            filtered_transactions = filtered_transactions
                        print("Распечатываю итоговый список транзакций...")
                      counter_category = get_filter_transaction_category(filtered_transactions)
                        print(f"Всего банковских операций в выборке: {counter_category}")

                        else:
                        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")














if __name__ == "__main__":
    main()
