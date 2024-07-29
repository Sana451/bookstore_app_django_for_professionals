from django.urls import reverse, resolve
from django.test import Client
import pytest
from pytest_django.asserts import assertTemplateUsed

from pages.views import HomePageView


@pytest.fixture(scope="function")
def response(client: Client):
    url = reverse("home")
    response = client.get(url)
    return response


def test_url_exists_at_correct_location(response):
    assert response.status_code == 200


def test_homepage_url_name(response):
    assert response.status_code == 200


def test_homepage_template(response):
    assertTemplateUsed(response, "home.html")


def test_homepage_contains_correct_html(response):
    assert "home page" in response.content.decode()


def test_homepage_does_not_contain_incorrect_html(response):
    assert "Hi there! I should not be on the page." not in response.content.decode()


def test_homepage_url_resolves_homepage_view():
    view = resolve("/")
    assert view.func.__name__ == HomePageView.as_view().__name__
