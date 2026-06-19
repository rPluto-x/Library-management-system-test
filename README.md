# Library Management System — Test Suite

A fully automated test suite for a Library Management System built with Python and Pytest.

---

## Project Structure

LIBRARY MANAGEMENT SYSTEM/
├── src/
│   ├── __init__.py
│   └── library.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   └── test_library.py
├── .gitignore
├── pytest.ini
└── README.md

---

## What's Being Tested

### Book Class
- Availability checking
- Borrowing and returning books
- Available copy count
- Book attributes
- Edge case: borrow all copies then return one
- Exception handling for invalid operations
- Parameterized availability tests

### Library Class
- Library name verification
- Adding and removing books
- Finding books by ISBN
- Total book count
- Mocked external API call
- Exception handling

---

## Test Stats

| Metric | Result |
|---|---|
| Total Tests | 23 |
| Passed | 23 |
| Failed | 0 |
| Coverage | 100% |

---

## Tech Stack

- Python
- Pytest
- unittest.mock
- pytest-cov

---

## Running the Tests

bash
pytest
pytest -v
pytest --cov=src --cov-report=term-missing
pytest -m book_test
pytest -m library_test
pytest -m excep


---

## Markers

| Marker | Description |
|---|---|
| `book_test` | All book tests |
| `library_test` | All library tests |
| `avail_test` | Availability tests |
| `borrow_test` | Borrow tests |
| `return_test` | Return tests |
| `book_details` | Book attribute tests |
| `borrow_and_return` | Borrow and return edge case |
| `library_details` | Library attribute tests |
| `add_remove` | Add and remove tests |
| `find_book` | Find book tests |
| `total_books` | Total book count tests |
| `fetch_book_info` | Mocked API tests |
| `excep` | All exception tests |