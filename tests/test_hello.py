from src.hello import greet
import pytest

def test_greet_normal():
    assert greet("Binay") == "Hello, Binay!"

def test_greet_empty():
    assert greet("") == "Hello, !"

def test_greet_type_error():
    with pytest.raises(TypeError):
        greet(123)
