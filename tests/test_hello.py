from src.hello import greet


def test_greet():
    assert greet("Binay") == "Hello, Binay"


def test_greet_empty():
    assert greet("") == "Hello, World"
