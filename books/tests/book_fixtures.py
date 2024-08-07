import pytest

from books.models import Book


@pytest.fixture(scope="function")
def new_book():
    return Book.objects.create(
        title="Harry Potter",
        author="JK Rowling",
        price="25.00",
    )
