import pytest

from django.test import Client
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

from book_fixtures import new_book


@pytest.mark.django_db
def test_book_list_view(new_book, client: Client):
    response = client.get(reverse("book_list"))
    assert response.status_code == 200
    assert "Harry Potter" in response.content.decode()
    assertTemplateUsed(response, "books/book_list.html")


@pytest.mark.django_db
def test_book_detail_view(new_book, client: Client):
    response = client.get(new_book.get_absolute_url())
    no_response = client.get("/books/12345/")
    assert response.status_code == 200
    assert no_response.status_code == 404
    assert "Harry Potter" in response.content.decode()
    assertTemplateUsed(response, "books/book_detail.html")
