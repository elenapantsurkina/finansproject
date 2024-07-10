import pytest

from src.decorators import log, my_function


# def test_log_er():
#     with pytest.raises(ZeroDivisionError):
#         my_function(2, 0)


def test_log(capsys):
    print(my_function(2, 1))
    captured = capsys.readouterr()
    assert captured.out == "2.0\n"


def test_log_positiv():
    @log(filename="mylog.txt")
    def my_function(x, y):
        return x / y
    result = my_function(2, 1)
    assert result == 2.0
