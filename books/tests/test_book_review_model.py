import pytest

from book_fixtures import new_book, new_review_user
from books.models import Review


@pytest.mark.django_db
def test_book_have_review(new_book, new_review_user):
    review = Review.objects.create(
        book=new_book,
        review="An excellent review",
        author=new_review_user
    )
    assert review.author == new_review_user
    assert review.book == new_book
