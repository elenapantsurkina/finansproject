import pytest

from src.widget import mask_account_card, get_data


@pytest.mark.parametrize('string, expected_result', [
    ('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'), ('Счет 64686473678894779589', 'Счет **9589')])
def test_mask_account_card(string, expected_result):
    assert mask_account_card(string) == expected_result


@pytest.fixture
def data():
    return '2018-07-11T02:26:18.671407'


def test_get_data(data):
    assert get_data(data) == '11.07.2018'
