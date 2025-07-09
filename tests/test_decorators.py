import pytest
import os
from src.decorators import log


@pytest.fixture(autouse=True)
def cleanup():
    if os.path.exists("mylog.txt"):
        os.remove("mylog.txt")
    yield
    if os.path.exists("mylog.txt"):
        os.remove("mylog.txt")

@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

def test_my_function_success():
    result = my_function(1, 2)
    assert result == 3
    with open("mylog.txt", "r") as f:
        logs = f.read()
    assert "my_function ok" in logs

@log(filename="mylog.txt")
def my_function_with_error(x, y):
    return x / y

def test_my_function_error(capsys):
    with pytest.raises(ZeroDivisionError):
        my_function_with_error(1, 0)

    with open("mylog.txt", "r") as f:
        logs = f.read()
    assert "my_function_with_error error: ZeroDivisionError. Inputs: (1, 0), {}" in logs

@log
def my_function_console(x, y):
    return x + y

def test_my_function_console(capsys):
    my_function_console(3, 4)
    captured = capsys.readouterr()
    assert "my_function_console ok" in captured.out