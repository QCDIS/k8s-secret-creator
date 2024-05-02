import pytest

from flask import *


def test_request_example(client_authenticated):
    data = {
        "password": "c3VwZXJTZWNyZXRQNCQkdzByZA==",
        "username": "YWxpY2U=",
        }

    response = client_authenticated.post(
        '/k8s-secret-creator/1.0.0/',
        data=json.dumps(data),
        headers={
            'accept': 'application/json',
            'Content-Type': 'application/json',
            }
        )
    assert response.status_code == 200
