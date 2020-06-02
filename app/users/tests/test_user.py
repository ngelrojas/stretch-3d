import pytest
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.urls import reverse

URL_USER_DETAILS = reverse("user:user-details", (), {"pk": 2})


class UserManagerTests(TestCase):
    """test manager user"""

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email="me@ngelrojasp.com", password="me123456")
        self.assertEqual(user.email, "me@ngelrojasp.com")
        self.assertTrue(user.is_activate)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser("admin@ngelrojasp.com", "admin2020")
        self.assertEqual(admin_user.email, "admin@ngelrojasp.com")
        self.assertTrue(admin_user.is_activate)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

    @pytest.mark.django_db
    def test_create_user_pytest(self):
        """test using pytest"""
        User = get_user_model()
        User.objects.create_user("me@ngelrojasp.com", "me123456")
        assert User.objects.count() == 1

    @pytest.mark.django_db
    def test_view_pytest(self):
        User = get_user_model()
        user = User.objects.create_user("me@ngelrojasp.com", "me123456")
        url = reverse("user:user-details", (), {"pk", user.pk})
        response = self.client.get(URL_USER_DETAILS)
        assert response.status_code == 200
