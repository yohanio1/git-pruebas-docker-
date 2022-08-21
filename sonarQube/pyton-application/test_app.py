
# content of test_sample.py
from xxlimited import foo


def inc(x):
    return x + 2

def capital_case(x):
    return x.capitalize()


def test_capital():
    assert capital_case("foo") == "Foo"

def test_answer():
    assert inc(3) == 5


