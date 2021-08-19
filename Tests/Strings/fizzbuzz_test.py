import Strings.fizzbuzz as f

def test_fizzbuzz_1():
    assert f.fizzbuzz(50) == "Buzz"

def test_fizzbuzz_2():
    assert f.fizzbuzz(15) == "FizzBuzz"

def test_fizzbuzz_3():
    assert f.fizzbuzz(33) == "Fizz"

def test_fizzbuzz_4():
    assert f.fizzbuzz(2) == ""