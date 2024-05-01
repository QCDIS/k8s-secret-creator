import connexion

from k8s_secret_creator.models.created_secret import CreatedSecret  # noqa: E501
from k8s_secret_creator import util


def add_secret(body=None):  # noqa: E501
    """add a secret

    Create a new secret containing the provided data # noqa: E501

    :param body: Secret data
    :type body: dict | bytes

    :rtype: CreatedSecret
    """
    if connexion.request.is_json:
        body = Dict[str, bytearray].from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
