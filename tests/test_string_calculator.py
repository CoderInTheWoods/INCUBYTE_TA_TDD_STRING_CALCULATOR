import pytest

from calc.string_calculator import add
from calc.string_calculator import GetCalledCount

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
    assert add("//#\n1#2#3#4#5") == 15

# TEST 7: Throw exception on negative numbers
def test_stringcalculator_must_throw_exception_on_negative_numbers():
    with pytest.raises(Exception, match="negatives not allowed : [-2, -4]"):
        assert add("//#\n1#-2#3#-4#5")

# TEST 8: Return the count of number of times add() was invoked
def test_stringcalculator_must_return_count_of_calls_to_add_function():
    assert GetCalledCount() == 10

# TEST 9: Ignore numbers greater than 1000
def test_stringcalculator_must_ignore_numbers_greater_than_thousand():
    assert add("2,1002") == 2
    assert add("1001,1001") == 0

# TEST 10: Allow delimiters of any length
def test_stringcalculator_must_allow_delimiters_of_any_legth():
    assert add("//[***]\n1***2") == 3
    assert add("//[@@]\n1@@2@@3@@4@@5") == 15

# TEST 10: Allow multiple delimiters
def test_stringcalculator_must_allow_multiple_delimiters():
    assert add("//[***][###]\n1***2###3") == 6
    assert add("//[@][#][$]\n1@2#3$4@5") == 15
