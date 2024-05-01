#!/usr/bin/env python3

import connexion

from k8s_secret_creator import encoder


def main():
    app = connexion.App(__name__, specification_dir='openapi/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml', arguments={'title': 'K8s secret creator'}, pythonic_params=True)
    app.run(port=8080)


if __name__ == '__main__':
    main()
