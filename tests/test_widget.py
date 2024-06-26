import pytest

from src.widget import mask_account_card, get_data


@pytest.mark.parametrize(
    "string, expected_result",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
    ],
)
def test_mask_account_card(string, expected_result):
    assert mask_account_card(string) == expected_result


def test_get_data(data):
    assert get_data(data) == "11.07.2018"
