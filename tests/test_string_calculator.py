import pytest

from calc.string_calculator import add

# TEST 1: Return 0 on empty string
def test_stringcalculator_must_return_zero_on_empty_string():
    assert add("") == 0

# TEST 2: Return numeric value on single number string
def test_stringcalculator_must_return_numeric_value_on_single_number_string():
    assert add("2") == 2