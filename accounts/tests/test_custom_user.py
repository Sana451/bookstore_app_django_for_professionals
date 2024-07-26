import pytest
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.mark.django_db
class TestCustomUser:

    def test_create_user(self):
        user = User.objects.create_user(username="will", email="will@email.com", password="testpass123")
        assert user.username == "will"
        assert user.email == "will@email.com"
        assert user.is_active is True
        assert user.is_staff is False
        assert user.is_superuser is False

    def test_create_superuser(self):
        user = User.objects.create_superuser(username="superadmin", email="superadmin@mail.com", password="testpwd")
        assert user.username == "superadmin"
        assert user.email == "superadmin@mail.com"
        assert user.is_staff is True
        assert user.is_active is True
        assert user.is_superuser is True
