# coding: utf-8

from setuptools import setup, find_packages

NAME = "k8s_secret_creator"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion",
    "swagger-ui-bundle>=0.0.2"
]

setup(
    name=NAME,
    version=VERSION,
    description="K8s secret creator",
    author_email="gabriel.pelouze@lifewatch.eu",
    url="https://github.com/QCDIS/k8s-secret-creator",
    keywords=["Swagger", "K8s secret creator"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['k8s_secret_creator=k8s_secret_creator.__main__:main']},
    long_description="""\
    A simple API to add secrets to Kubernetes
    """
)
