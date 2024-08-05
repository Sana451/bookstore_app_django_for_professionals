import pytest
from pytest_django.asserts import assertTemplateUsed
from django.contrib.auth import get_user_model
from django.template.response import TemplateResponse
from django.urls import reverse, resolve
from django.test import Client


User = get_user_model()
username = "newuser"
email = "newuser@email.com"


@pytest.fixture(scope="function")
def response(client: Client):
    url = reverse("account_signup")
    response = client.get(url)
    return response


@pytest.mark.django_db
def test_signup_template(response: TemplateResponse):
    assert response.status_code == 200
    assert "Sign Up" in response.content.decode()
    assert "Hi there! I should not be on the page." not in response.content.decode()
    assertTemplateUsed(response, "account/signup.html")


@pytest.mark.django_db
def test_signup_form(response: TemplateResponse):
    new_user = User.objects.create_user(username, email)
    assert User.objects.all().count() == 1
    assert User.objects.all()[0].username, username
    assert User.objects.all()[0].email, email
