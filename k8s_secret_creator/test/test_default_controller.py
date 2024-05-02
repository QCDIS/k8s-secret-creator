import pytest

from flask import *


def test_request_example(client_authenticated):
    body = {}

    response = client_authenticated.post(
        '/k8s-secret-creator/1.0.0',
        data=json.dumps(body),
        )
    assert response.status_code == 200
