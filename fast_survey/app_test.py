"""Main app test."""
from http import HTTPStatus

import pytest
from fastapi.testclient import TestClient


@pytest.fixture()
def client():
    """App startup."""
    from fast_survey.main import app
    print(app.servers)
    yield TestClient(app)


def test_home_get(client: TestClient) -> None:
    """Test users_surveys."""
    with client as client:
        response = client.get('/')
        assert response.status_code == HTTPStatus.OK
