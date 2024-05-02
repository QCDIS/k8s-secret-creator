import os
from connexion.exceptions import OAuthProblem


def check_apikey_auth(token):
    if token != os.getenv('API_TOKEN', None):
        raise OAuthProblem("Invalid token")
    else:
        return {"active": True}
