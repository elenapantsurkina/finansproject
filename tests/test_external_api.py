from unittest.mock import patch, MagicMock
import json
from src.external_api import get_transaction_sum_rub

@patch('src.external_api.requests')
def test_get_transaction_sum_rub(mock_get):
     transaction = {"operationAmount": {"amount": "67314.70", "currency": {"code": "RUB"}}}
     mock_get.return_value.json.return_value = {"result": 67314.70}
     assert get_transaction_sum_rub(transaction) == 67314.70

@patch('src.external_api.requests')
def test_get_transaction_sum_rub(mock_get):
    mock_resp = MagicMock()
    mock_resp.status_code = 200
    mock_resp.json.return_value = {"result": 5917366.82}
    transaction = {"operationAmount": {"amount": "67314.70", "currency": {"code": "USD"}}}
    mock_get.get.return_value = mock_resp
    assert get_transaction_sum_rub(transaction) == 5917366.82
