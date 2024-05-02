import os

import pytest

from k8s_secret_creator.__main__ import create_app


@pytest.fixture
def app():
    app = create_app()
    return app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def client_authenticated(app):
    os.environ['API_TOKEN'] = 'test_api_token'
    os.environ['K8S_NAMESPACE'] = 'default'
    os.environ['SECRET_PREFIX'] = 'ksc-'
    c = app.test_client()
    c.headers = {
        'X-Auth': 'test_api_token',
        }
    return c


@pytest.fixture
def runner(app):
    return app.test_cli_runner()
