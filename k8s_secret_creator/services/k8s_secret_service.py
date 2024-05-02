import os
import uuid

from kubernetes import client, config
import kubernetes.client
from kubernetes.config.config_exception import ConfigException

from k8s_secret_creator.models.created_secret import CreatedSecret
from k8s_secret_creator.models.secret_data import SecretData


def get_namespace():
    return os.getenv('K8S_NAMESPACE', None)


def gen_secret_name():
    prefix = os.getenv('SECRET_PREFIX', 'ksc-')
    secret_id = str(uuid.uuid4())
    return f'{prefix}{secret_id}'


def gen_secret(secret_data: SecretData):
    return kubernetes.client.V1Secret(
        metadata={
            'name': gen_secret_name(),
            },
        data=secret_data,
        )


def create_secret(secret_data: SecretData):
    """create a secret in k8s

    :param secret_data: Secret data
    :type secret_data: dict

    :rtype: CreatedSecret
    """

    try:
        config.load_kube_config()
    except ConfigException:
        config.load_incluster_config()

    secret = gen_secret(secret_data)

    v1 = client.CoreV1Api()
    v1.create_namespaced_secret(get_namespace(), secret)

    return CreatedSecret(secret.metadata.get('name'))
