import pytest

from myapp.mymodule.funcs import *

@pytest.mark.easy_operation
def test_add():
    # This test will fail.
    assert add(4, 8) == 14

@pytest.mark.easy_operation
def test_subtract():
    assert subtract(3, 6) == -3

@pytest.mark.difficult_operation
def test_multiply():
    assert multiply(4, 5) == 20

@pytest.mark.difficult_operation
def test_divide():
    assert divide(56, 8) == 7

@pytest.mark.easy_operation
def test_calculate_area():
    assert calculate_area(4) == 16  # 4^2 = 16

# Add a test using the last two digits of student ID
@pytest.mark.easy_operation
def test_calculate_area_45():
    assert calculate_area(7.416) == 54.99705600000001
