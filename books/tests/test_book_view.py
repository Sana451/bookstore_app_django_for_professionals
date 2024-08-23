from django.contrib.auth.models import Permission
from django.test import Client
from django.urls import reverse
import pytest
from pytest_django.asserts import assertTemplateUsed

from book_fixtures import new_book
from book_fixtures import new_user
from books.models import Review


@pytest.mark.django_db
def test_not_logged_in_user_cant_see_book_list(client: Client, new_user):
    response = client.get(reverse("book_list"))
    assert response.status_code == 302
    assert response.url == "/accounts/login/?next=/books/"


@pytest.mark.django_db
def test_only_logged_in_user_can_see_book_list(client: Client, new_book, new_user):
    client.login(username="user1", password="user1password")
    response = client.get(reverse("book_list"))
    assert response.status_code == 200
    assert "Harry Potter" in response.content.decode()


@pytest.mark.django_db
def test_only_users_with_special_permissions_can_see_book_detail_view(client: Client, new_book, new_user):
    client.login(username="user1", password="user1password")
    new_user.user_permissions.add(Permission.objects.get(codename="special_status"))
    response = client.get(new_book.get_absolute_url())
    no_response = client.get("/books/12345/")
    assert response.status_code == 200
    assert no_response.status_code == 404
    assert "Harry Potter" in response.content.decode()
    assertTemplateUsed(response, "books/book_detail.html")


@pytest.mark.django_db
def test_users_without_special_permissions_cant_see_book_detail_view(client: Client, new_book, new_user):
    client.login(username="user1", password="user1password")
    response = client.get(new_book.get_absolute_url())
    assert response.status_code == 403


@pytest.mark.django_db
def test_book_detail_view_contains_review(new_book, new_user, client: Client):
    Review.objects.create(
        book=new_book,
        review="An excellent review",
        author=new_user
    )
    client.force_login(new_user)
    new_user.user_permissions.add(Permission.objects.get(codename="special_status"))
    response = client.get(new_book.get_absolute_url())
    assert response.status_code == 200
    assert "An excellent review" in response.content.decode()
