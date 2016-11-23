from fizzbuzz import FizzBuzz

def test_fizz():
    for x in [3,6]:
        assert FizzBuzz.FIZZ == FizzBuzz.fizzbuzz(x)

def test_buzz():
    for x in [5,10]:
        assert FizzBuzz.BUZZ == FizzBuzz.fizzbuzz(x)

def test_fizzbuzz():
    for x in [15,30]:
        assert FizzBuzz.FIZZ+FizzBuzz.BUZZ in FizzBuzz.fizzbuzz(x)

def test_number():
    for x in [1,2,4]:
        assert str(x) == FizzBuzz.fizzbuzz(x)