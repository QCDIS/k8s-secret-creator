# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from k8s_secret_creator.models.created_secret import CreatedSecret  # noqa: E501
from k8s_secret_creator.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_add_secret(self):
        """Test case for add_secret

        add a secret
        """
        body = None
        response = self.client.open(
            '/k8s-secret-creator/1.0.0/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
