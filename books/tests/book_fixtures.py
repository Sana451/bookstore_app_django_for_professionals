import pytest
from django.contrib.auth import get_user_model

from books.models import Book

User = get_user_model()


@pytest.fixture(scope="function")
def new_book():
    return Book.objects.create(
        title="Harry Potter",
        author="JK Rowling",
        price="25.00",
    )


@pytest.fixture(scope="function")
def new_review_user():
    return User.objects.create(
        username="reviewuser",
        email="reviewuser@email.com",
        password="testpass123",
    )
