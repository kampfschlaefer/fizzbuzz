
#import pytest

from fizzbuzz.basic import fizzbuzz as basic_fizzbuzz


def fizzbuzz_check(fizzbuzz):
    for i in range(100):
        result = fizzbuzz(i)
        if i % 3 == 0:
            assert 'Fizz' in result
        if i % 5 == 0:
            assert 'Buzz' in result
        if i % 3 and i % 5:
            assert int(result) == i


def test_basic_fizzbuzz():
    fizzbuzz_check(basic_fizzbuzz)
