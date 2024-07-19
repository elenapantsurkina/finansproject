from unittest.mock import Mock

import pandas as pd

from unittest.mock import patch
from unittest.mock import mock_open
from src.reader_file import reader_file_transaction_csv

from src.reader_file import reader_file_transaction_excel


@patch('csv.reader')
def test_reader_file_transaction_csv(mock_reader):
    m = mock_open()
    mock_reader.return_value = iter ([
        ["id", "state", "date", "amount", "currency_name", "currency_code", "from", "to", "description"],
        ["650703", "EXECUTED", "2023-09-05T11:30:32Z", "16210", "Sol", "PEN", "Счет 58803664561298323391",
        "Счет 39745660563456619397", "Перевод организации"]])

    with patch('builtins.open', m) as mocked_open:
        assert reader_file_transaction_csv('transaction.csv') == [{
                'id': '650703',
            'state': 'EXECUTED',
            'date': '2023-09-05T11:30:32Z',
            'operationAmount':
            {'amount': '16210', 'currency':
                    {'name': 'Sol', 'code': 'PEN'}},
            'description': 'Перевод организации',
            'from': 'Счет 58803664561298323391',
            'to': 'Счет 39745660563456619397'}]

        mocked_open.assert_called_with('transaction.csv', 'r', encoding='utf-8')


# def test_reader_file_transaction_csv():
#     mock_read_csv = Mock(result_value={
#             'id': '650703',
#             'state': 'EXECUTED',
#             'date': '2023-09-05T11:30:32Z',
#             'operationAmount':
#             {'amount': '16210', 'currency':
#                     {'name': 'Sol', 'code': 'PEN'}},
#             'description': 'Перевод организации',
#             'from': 'Счет 58803664561298323391',
#             'to': 'Счет 39745660563456619397'})
#     result = mock_read_csv
#     assert reader_file_transaction_csv(result) == ({
#             'id': '650703',
#             'state': 'EXECUTED',
#             'date': '2023-09-05T11:30:32Z',
#             'operationAmount':
#             {'amount': '16210', 'currency':
#                     {'name': 'Sol', 'code': 'PEN'}},
#             'description': 'Перевод организации',
#             'from': 'Счет 58803664561298323391',
#             'to': 'Счет 39745660563456619397'})
#
# @patch('csv.reader')
# def test_reader_file_transaction_csv(mock_reader):
#
#     mock_reader.return_value = [{
#         'id': '650703',
#         'state': 'EXECUTED',
#         'date': '2023-09-05T11:30:32Z',
#         'operationAmount':
#             {'amount': '16210',
#              'currency': {'name': 'Sol', 'code': 'PEN'}},
#         'description': 'Перевод организации',
#         'from': 'Счет 58803664561298323391',
#         'to': 'Счет 39745660563456619397'}]
#
#     result = reader_file_transaction_csv('..\\data\\transactions.csv')
#     expected_result = [{
#     'id': '650703',
#     'state': 'EXECUTED',
#     'date': '2023-09-05T11:30:32Z',
#     'operationAmount':
#         {'amount': '16210',
#          'currency': {'name': 'Sol', 'code': 'PEN'}},
#     'description': 'Перевод организации',
#     'from': 'Счет 58803664561298323391',
#     'to': 'Счет 39745660563456619397'}]
#     assert result == expected_result
#
#
# def test_reader_file_transaction_csv():
#     with patch('csv.reader') as mock:
#         mock_response = Mock()
#
#         mock_response.return_value = [{'id': '650703', 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z'}]
#         assert reader_file_transaction_csv('transaction.csv') == [{'id': '650703', 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z'}]
# #
# #
# @patch("pandas.read_excel")
# def test_reader_file_transaction_excel(mock_read_excel):
#     mock_read_excel.return_value = [{'id': 4699552.0,
#          'state': 'EXECUTED',
#          'date': '2022-03-23T08:29:37Z',
#          'amount': 23423.0,
#          'currency_name': 'Peso',
#          'currency_code': 'PHP',
#          'from': 'Discover 7269000803370165',
#          'to': 'American Express 1963030970727681',
#          'description': 'Перевод с карты на карту'}]
#     result = reader_file_transaction_excel("transactions_excel.xlsx")
#     expected_result = [{'id': 4699552.0,
#          'state': 'EXECUTED',
#          'date': '2022-03-23T08:29:37Z',
#          'amount': 23423.0,
#          'currency_name': 'Peso',
#          'currency_code': 'PHP',
#          'from': 'Discover 7269000803370165',
#          'to': 'American Express 1963030970727681',
#          'description': 'Перевод с карты на карту'}]
#
#     assert result == expected_result
