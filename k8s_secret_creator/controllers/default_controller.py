from k8s_secret_creator.models.created_secret import CreatedSecret
from k8s_secret_creator.models.secret_data import SecretData
from k8s_secret_creator.services.k8s_secret_service import create_secret


def add_secret(body=None):
    """add a secret

    Create a new secret containing the provided data

    :param body: Secret data
    :type body: dict | bytes

    :rtype: dict
    """
    body = SecretData.from_dict(body)
    created_secret = create_secret(body)
    return created_secret.to_dict()
