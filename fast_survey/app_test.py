"""Main app test."""
import asyncio
from http import HTTPStatus

import pytest
from httpx import AsyncClient

from fast_survey.main import app, settings


@pytest.fixture(scope='module')
def event_loop():
    """Fix pytest async module error."""
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope='module')
async def client():
    """Fixture for creating database."""
    settings.database_url = settings.database_url_test
    test_client: AsyncClient = AsyncClient(app=app, base_url='http://test')
    yield test_client
    await test_client.aclose()


async def test_users_surveys(client: AsyncClient) -> None:
    """Test users_surveys route."""
    response = await client.get('/')
    assert response.status_code == HTTPStatus.OK


async def test_create_user_survey(client: AsyncClient) -> None:
    """Test creation of a user survey with valid data."""
    data = {
        'name': 'tester',
        'gender': 'male',
        'age': 18,
    }
    response = await client.post('/create_survey/', json=data)
    assert response.status_code == HTTPStatus.CREATED
    assert response.json()['name'] == data['name']


async def test_cant_create_user_survey(client: AsyncClient) -> None:
    """Test creation of a user survey with invalid data."""
    data = {
        'gender': '',
        'age': 0,
    }
    response = await client.post('/create_survey/', json=data)
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
