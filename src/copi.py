from src.utils import get_transactions_list
from src.reader_file import reader_file_transaction_csv, reader_file_transaction_excel
from src.processing import filter_by_state, sort_by_date
from src.filter_transactions import get_filter_transaction
from src.filter_transactions_category import get_filter_transaction_category
from src.widget import mask_account_card, get_data


def main():
    while True:
        user_input = input(
            "Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n"
            "Выберите необходимый пункт меню:\n"
            "1. Получить информацию о транзакциях из JSON-файла\n"
            "2. Получить информацию о транзакциях из CSV-файла\n"
            "3. Получить информацию о транзакциях из XLSX-файла\n"
        )
        if user_input not in ["1", "2", "3"]:
            print("Вами не выбран доступный формат файла")
            continue
        elif user_input == "1":
            print("Для обработки выбран JSON-файл")
            # continue
            transactions = get_transactions_list("../data/operations.json")
        elif user_input == "2":
            print("Для обработки выбран CSV-файл")
            # continue
            transactions = reader_file_transaction_csv("../data/transactions.csv")
        elif user_input == "3":
            print("Для обработки выбран XLCX-файл")
            # continue
            transactions = reader_file_transaction_excel("../data/transactions_excel.xlsx")
        loop = True
        while loop:
            input_user_state = input(
               "Введите статус, по которому необходимо выполнить фильтрацию.\n "
                "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
            ).upper()
            if input_user_state not in ["EXECUTED", "CANCELED", "PENDING"]:
                print(f"Статус операции {input_user_state} не доступен.")
                continue
            else:
               print(f"Операции отфильтрованы по статусу{input_user_state}")
            filtered_transactions = filter_by_state(transactions, input_user_state)
            loop = False

        user_input_data = input("Отсортировать операции по дате? Да/Нет\n").upper()
        if user_input_data == "ДА":
            input_user_sort = input("Отсортировать по возрастанию/по убыванию\n").upper()
            if input_user_sort == "ПО ВОЗРАСТАНИЮ":
                filtered_transactions = sort_by_date(filtered_transactions)
            else:
                filtered_transactions = sort_by_date(filtered_transactions, False)

        input_user_rub = input("Выводить только рублевые тразакции? Да/Нет\n").upper()
        if input_user_rub == "ДА":
            filtered_transactions = [
                t for t in filtered_transactions if t["operationAmount"]["currency"]["code"] == "RUB"
            ]

        input_user_filter_description = input(
            "Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n"
        ).upper()
        if input_user_filter_description == "ДА":
            input_user_filter_description = input("Введите категорию фильтрации: ").capitalize()
            filtered_transactions = get_filter_transaction(
                filtered_transactions, bank_op=input_user_filter_description
            )
            print("Распечатываю итоговый список транзакций...")
            if filtered_transactions:
                counter_category = get_filter_transaction_category(filtered_transactions)
                print(
                    f"Всего банковских операций в выборке: {input_user_filter_description}: {counter_category[input_user_filter_description]}"
                )
                # print(filtered_transactions)
                for trans in filtered_transactions:
                    print(f"Дата: {get_data(trans['date'])}, {trans['description']}")
                    if trans.get("from"):
                        print(f"Счет: {mask_account_card(trans['from'])} -> Счет: {mask_account_card(trans['to'])}")
                    else:
                        print(f"Счет: {mask_account_card(trans['to'])}")
                    print(f"Сумма: {trans['operationAmount']['amount']}")
                break

            else:
                print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")

        else:
            print("Распечатываю итоговый список транзакций...")
            print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")
            for trans in filtered_transactions:
                print(f"Дата: {get_data(trans['date'])}, {trans['description']}")
                if trans.get("from"):
                    print(f"Счет: {mask_account_card(trans['from'])} -> Счет: {mask_account_card(trans['to'])}")
                else:
                    print(f"Счет: {mask_account_card(trans['to'])}")
                print(f"Сумма: {trans['operationAmount']['amount']}")
            # print(filtered_transactions)
            break

    return


if __name__ == "__main__":
    main()
