import pytest
from django.test import TestCase
from django.test.client import Client
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.urls import reverse

URL_USER_DETAILS = reverse("user:user-details", (), {"pk": 2})
URL_CREATE_USER = reverse("user:create")


class UserManagerTests(TestCase):
    """test manager user"""

    def setUp(self):
        self.client = Client()

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
    def test_create_user_url_pytest(self):
        """create user throught end-point"""
        payload = {
            "fist_name": "ngel",
            "last_name": "rojas",
            "email": "me@ngelrojasp.com",
            "password": "me123456",
        }
        response = self.client.post(URL_CREATE_USER, payload)
        assert response.status_code == 201
