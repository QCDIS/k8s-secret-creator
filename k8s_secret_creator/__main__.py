from k8s_secret_creator.app import create_app


def main():
    app = create_app()
    app.run(host='0.0.0.0', port=8080)


if __name__ == '__main__':
    main()
