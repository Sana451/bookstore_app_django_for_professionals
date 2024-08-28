from django.urls import reverse
from django.test import Client
import pytest
from pytest_django.asserts import assertTemplateUsed

from pages.views import AboutPageView
from book_fixtures import new_user


@pytest.fixture(scope="function")
def response(client: Client):
    url = reverse("about")
    response = client.get(url)
    return response


def test_about_page_status_code(response):
    assert response.status_code == 200


def test_about_page_template(response, new_user):
    assertTemplateUsed(response, "about.html")


def test_about_page_contains_correct_html(response):
    assert "About Page" in response.content.decode()


def test_about_page_does_not_contain_incorrect_html(response):
    assert "Hi there! I should not be on the page." not in response.content.decode()


def test_about_page_url_resolves_home_page_view(response):
    assert response.resolver_match.func.view_class == AboutPageView
