
import pytest

from fizzbuzz.basic import fizzbuzz as basic_fizzbuzz


algorithms = [basic_fizzbuzz]


@pytest.mark.parametrize('algo', algorithms)
def test_check_three(algo):
    for i in range(0, 100, 3):
        assert 'Fizz' in algo(i)


@pytest.mark.parametrize('algo', algorithms)
def test_check_fives(algo):
    for i in range(0, 100, 5):
        assert 'Buzz' in algo(i)


@pytest.mark.parametrize('algo', algorithms)
def test_check_numbers(algo):
    for i in range(0, 100):
        if i % 3 and i % 5:
            assert algo(i) == str(i)
