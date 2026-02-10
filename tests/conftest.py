import pytest
from rest_framework.test import APIClient
from serializerAndapiview.models import Post


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture()
def post():
    return Post.objects.create(title="Test post", content="Test post content")
