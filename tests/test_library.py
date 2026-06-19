import pytest
from unittest.mock import patch
from src.library import Book, Library

#Test for Book
@pytest.mark.book_test
class TestBook:
    #Test if is_available() works properly when books are sufficient
    @pytest.mark.avail_test
    def test_is_available_true(self, book_1):
        result = book_1.is_available()
        assert result == True

    #Test if is_available() works properly when there are no books
    @pytest.mark.avail_test
    def test_is_available_false(self, book_2):
        result = book_2.is_available()
        assert result == False

    #Parametrizer for the next test
    @pytest.mark.avail_test
    @pytest.mark.parametrize("copies, borrowed, expected", [
        (50, 0, True),
        (0, 0, False),
        (1, 1, False),
        (5, 3, True),
        (2, 2, False),
    ])

    #Test if is_available() works properly using parametrizer with multiple values
    def test_is_available_param(self, copies, borrowed, expected):
        book = Book("Test", "Author", "123", copies)
        book.borrowed = borrowed
        assert book.is_available() == expected

    #Test if borrow() works properly when books are sufficient
    @pytest.mark.borrow_test
    def test_borrow(self, book_1):  
        book_1.borrow()
        assert book_1.available_copies() == 49

    #Test if borrow() exception works properly
    @pytest.mark.borrow_test
    @pytest.mark.excep
    def test_borrow_excep(self, book_2):
        with pytest.raises(ValueError):
            book_2.borrow()

    #Test if return_book() works properly
    @pytest.mark.return_test
    def test_return_book(self, book_1):
        book_1.borrow()
        book_1.return_book()
        assert book_1.available_copies() == 50

    #Test if return_book() exception works properly
    @pytest.mark.return_test
    @pytest.mark.excep
    def test_return_book_excep(self, book_1):
        with pytest.raises(ValueError):
            book_1.return_book()

    #Test if available_copies() works properly
    @pytest.mark.avail_test
    def test_available_copies(self, book_1):
        assert book_1.available_copies() == 50

    #Test that details are created correctly
    @pytest.mark.book_details
    def test_book_details(self, book_1):
        assert book_1.title == "book_1"
        assert book_1.author == "author_2"
        assert book_1.isbn == "9058"
        assert book_1.copies == 50

    #Test if return_books() works when all books have been borrowed
    @pytest.mark.borrow_and_return
    def test_borrow_all_return_one(self):
        book = Book("Test", "Author", "123", 2)
        book.borrow()
        book.borrow()
        assert book.is_available() == False
        book.return_book()
        assert book.is_available() == True


#Test for Library
@pytest.mark.library_test
class TestLibrary:
    #Test the name is correct
    @pytest.mark.library_details
    def test_lib_details(self, lib_1):
        assert lib_1.name == "Goodwill Library"
    
    #Test if add-book() works properly
    @pytest.mark.add_remove
    def test_add_book(self, lib_1, book_1):
        lib_1.add_book(book_1)
        assert lib_1.total_books() == 1

    #Test if add_book() exception works properly
    @pytest.mark.add_remove
    @pytest.mark.excep
    def test_add_book_excep(self, lib_1, book_1):
        lib_1.add_book(book_1)
        with pytest.raises(ValueError):
            lib_1.add_book(book_1)

    #Test if remove_book() works properly
    @pytest.mark.add_remove
    def test_remove_book(self, lib_1, book_1, book_2):
        lib_1.add_book(book_1)
        lib_1.add_book(book_2)
        lib_1.remove_book(book_2.isbn)
        assert lib_1.total_books() == 1

    #Test if remove_book() exception works properly
    @pytest.mark.add_remove
    @pytest.mark.excep
    def test_remove_book_excep(self, lib_1, book_1):
        with pytest.raises(ValueError):
            lib_1.remove_book(book_1.isbn)

    #Test if find_book() works properly
    @pytest.mark.find_book
    def test_find_book(self, lib_1, book_1):
        lib_1.add_book(book_1)
        assert lib_1.find_book(book_1.isbn) == book_1
        
    #Test if find_book() exception works properly
    @pytest.mark.find_book
    @pytest.mark.excep
    def test_find_book_excep(self, lib_1, book_1):
        with pytest.raises(ValueError):
            lib_1.find_book(book_1.isbn)

    #Test if total_books() works properly
    @pytest.mark.total_books
    def test_total_books(self, lib_1, book_1, book_2):
        lib_1.add_book(book_1)
        lib_1.add_book(book_2)
        assert lib_1.total_books() == 2

    #Test if fetch_book_info() works prpoperly using mock
    @pytest.mark.fetch_book_info
    def test_fetch_book_info(self, lib_1, book_1):
        lib_1.add_book(book_1)
        with patch("src.library.requests.get") as mock_get:
            mock_get.return_value.json.return_value = {"title": book_1.title}
            result = lib_1.fetch_book_info(book_1.isbn)
            assert result == book_1.title