import pytest

from book_fixtures import new_book


@pytest.mark.django_db
def test_book_listing(new_book):
    assert new_book.title == "Harry Potter"
    assert new_book.author == "JK Rowling"
    assert new_book.price == "25.00"
