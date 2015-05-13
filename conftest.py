import pytest

from django.contrib.auth.models import User
from django.test import Client


@pytest.fixture()
def client():
    return Client()


@pytest.fixture()
def basic_user():
    return User.objects.create_user('basic_user', '', 'test')
