import sys
from main import main
from io import StringIO
from unittest.mock import patch


def run_io_fun(input_str, func):
    with patch('sys.stdin', StringIO(input_str)):
        with patch('sys.stdout', new_callable=StringIO) as output:
            func()
            return output.getvalue().strip()


def test_case_1():
    input_data = """3
bfd
xwyz
qwerty"""
    expected = """Case #1: 10
Case #2: 153
Case #3: 36445"""
    result = run_io_fun(input_data, main)
    assert result == expected


def test_case_2():
    input_data = """2
ab
abc
"""
    expected = """Case #1: 0
Case #2: 10"""
    result = run_io_fun(input_data, main)
    assert result == expected
