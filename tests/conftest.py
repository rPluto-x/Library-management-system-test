import pytest
from src.library import Book, Library

@pytest.fixture
def book_1():
    return Book("book_1", "author_2", "9058", 50)

@pytest.fixture
def book_2():
    return Book("book_2", "author_2", "9788", 0)

@pytest.fixture
def lib_1():
    return Library("Goodwill Library")