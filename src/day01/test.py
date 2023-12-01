import pytest


from day01 import read_input, part1, part2, just_digits, replace_first_number, replace_last_number

def test_just_digits():
    assert just_digits("aaa3a  ads 4 da 21 ") == "3421"
    
def test_replace_first_number():
    assert replace_first_number("one1one") == "11one"
    assert replace_first_number("eightwo") == "8wo"

def test_replace_last_number():
    assert replace_last_number("one1one") == "one11"
    assert replace_last_number("eightwo") == "eigh2"

def test_part1():
    data = read_input("ex1")
    assert part1(data) == 142

def test_part2():
    data = read_input("ex2")
    assert part2(data) == 281
    
