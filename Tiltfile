k8s_yaml(helm('./helm/k8s-secret-creator'))

docker_build(
    'k8s-secret-creator',
    context='.',
    dockerfile='Dockerfile',
    live_update=[
        sync('./k8s_secret_creator/', '/app/k8s_secret_creator/'),
        sync('./requirements.txt', '/app/requirements.txt'),
        run('pip install --no-cache-dir -r /app/requirements.txt', trigger=['./requirements.txt'])
    ],
)

k8s_resource(
  workload='k8s-secret-creator',
  port_forwards=8080,
  links=['http://localhost:8080/k8s-secret-creator/1.0.0/ui'],
  )