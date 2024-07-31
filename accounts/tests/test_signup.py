import pytest
from pytest_django.asserts import assertTemplateUsed
from django.contrib.auth import get_user_model
from django.template.response import TemplateResponse
from django.urls import reverse, resolve
from django.test import Client

from accounts.forms import CustomUserCreationForm
from accounts.views import SignupPageView

User = get_user_model()


@pytest.fixture(scope="function")
def response(client: Client):
    url = reverse("signup")
    response = client.get(url)
    return response


def test_signup_template(response: TemplateResponse):
    assert response.status_code == 200
    assert "Sign Up" in response.content.decode()
    assert "Hi there! I should not be on the page." not in response.content.decode()
    assertTemplateUsed(response, "registration/signup.html")


def test_signup_form(response: TemplateResponse):
    form = response.context.get("form")
    assert isinstance(form, CustomUserCreationForm)
    assert "csrf_token" in response.context


def test_signup_view():
    view = resolve("/accounts/signup/")
    assert view.func.__name__ == SignupPageView.as_view().__name__
