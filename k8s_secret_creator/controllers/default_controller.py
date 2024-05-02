from k8s_secret_creator.models.created_secret import CreatedSecret
from k8s_secret_creator.models.secret_data import SecretData


def add_secret(body=None):
    """add a secret

    Create a new secret containing the provided data

    :param body: Secret data
    :type body: dict | bytes

    :rtype: CreatedSecret
    """
    body = SecretData.from_dict(body)
    return 'do some magic!'
