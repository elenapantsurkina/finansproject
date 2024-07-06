import pytest
from src.utils import get_transactions_list


def test_get_transactions_list():
    """проверка если передан пустой список"""
    assert transactions_list([]) == []


def test_get_transactions_list1():
    """ проверка если путь передан неверно"""
    assert get_transactions_list(my_file_path="..\\src\\operations.json") == []
