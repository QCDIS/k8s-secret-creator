# k8s secret creator

A simple API to create secrets into a Kubernetes namespace.

The only thing it can do is create a new Kubernetes secret from the key-value passed to the API endpoint. Once created, secrets cannot be listed or modified. The new secret's name is generated, and returned after creation.

## Development

### Set-up

```shell
conda env create -f environment.yaml
conda activate k8s-secret-creator
pip install -r requirements.txt
pip install -r test-requirements.txt
```

### Dev server

To run the server, please execute the following from the root directory:

```shell
minikube start
while read env; do export $env; done < .env.dev
python -m k8s_secret_creator
```

The Swagger UI is accessible at: http://localhost:8080/k8s-secret-creator/1.0.0/ui/

### Tests

To run the tests, execute:

```shell
minikube start
pytest
```

### Tilt

To run the service in Kubernetes or develop the Helm charts, run Tilt:

```shell
minikube start
tilt up
```

The swagger UI is accessible at: http://localhost:8080/k8s-secret-creator/1.0.0/ui/


## Deployment

We use Helm for the deployment.

Create a new file, `my-values.yaml`, containing at least the following lines:

```yaml
auth:
  api_token: '<a secure API token>'
```

Additional configuration such as ingress can be added to this values file. Refer to [./helm/k8s-secret-creator/values.yaml](./helm/k8s-secret-creator/values.yaml)

To deploy, run:

```shell
helm -n my-namespace upgrade --install --create-namespace k8s-secret-creator ./helm/k8s-secret-creator -f my-values.yaml
```
