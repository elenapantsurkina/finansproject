from unittest.mock import  patch
import requests
import json
from src.external_api import get_transaction_sum_rub

@patch('requests.get')
def test_get_transaction_sum_rub(mock_get):
    transaction = {"amount": 67314.70, "currency": "RUB"}
    mock_get.return_value.json.return_value = {"result": 67314.70}
    assert get_transaction_sum_rub(transaction) == 67314.70

@patch('requests.get')
def test_get_transaction_sum_rub(mock_get):
    transaction = {"amount": 56883.54, "currency": "USD"}
    mock_get.return_value.json.return_value = {"result": 3804126.56}
    assert get_transaction_sum_rub(transaction) == 3804126.56
