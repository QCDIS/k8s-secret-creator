FROM python:3.12-alpine

RUN mkdir -p /app
WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY k8s_secret_creator/ ./k8s_secret_creator/

EXPOSE 8080

ENTRYPOINT ["python3"]

CMD ["-m", "k8s_secret_creator"]