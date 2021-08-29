import pytest

from calc.string_calculator import add

# TEST 1: Return 0 on empty string
def test_stringcalculator_must_return_zero_on_empty_string():
    assert add("") == 0

# TEST 2: Return numeric value on single number string
def test_stringcalculator_must_return_numeric_value_on_single_number_string():
    assert add("2") == 2

# TEST 3: Return sum on two number string
def test_stringcalculator_must_return_sum_on_two_number_string():
    assert add("1,2") == 3

# TEST 4: Allow add() to handle unknown amount of numbers
def test_stringcalculator_must_handle_unknown_amount_of_numbers():
    assert add("1,2") == 3
    assert add("1,2,3,4,5") == 15

# TEST 5: Allow newline '\n' delimiter instead of commas ','
def test_stringcalculator_must_allow_newline_delimiter_instead_of_comma():
    assert add("1\n2") == 3
    assert add("1\n2\n3,4,5") == 15

# TEST 6: Support different delimiters | Example : "//;\n1;2" where';' is the delimiter
def test_stringcalculator_must_support_different_delimiters():
    assert add("//;\n1;2") == 3
    assert add("//#\n13#4#5") == 15