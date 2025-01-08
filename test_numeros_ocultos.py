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


def test_case_3():
    input_data = """2
banana
loolo
"""
    expected = """Case #1: 274
Case #2: 0"""
    result = run_io_fun(input_data, main)
    assert result == expected


def test_case_4():
    input_data = """2
abcabc
xyyxz
"""
    expected = """Case #1: 280
Case #2: 118"""
    result = run_io_fun(input_data, main)
    assert result == expected


def test_case_5():
    input_data = """1
abcdefghij"""
    expected = """Case #1: 8853086421"""
    result = run_io_fun(input_data, main)
    assert result == expected


def test_case_6():
    input_data = """1
abcdefg"""
    expected = """Case #1: 676950"""
    result = run_io_fun(input_data, main)
    assert result == expected


def test_case_7():
    input_data = """2
kkklll
abcxyzabc
"""
    expected = """Case #1: 0
Case #2: 7872289"""
    result = run_io_fun(input_data, main)
    assert result == expected


def test_case_8():
    input_data = """3
abbaabba
xyzxyzxyz
ppppqqqqrrr
"""
    expected = """Case #1: 0
Case #2: 7570
Case #3: 88534"""
    result = run_io_fun(input_data, main)
    assert result == expected
