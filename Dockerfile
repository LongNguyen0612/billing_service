FROM python:3.8.10
RUN pip install poetry
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
ENV PYTHONPATH=/app
COPY . /app
EXPOSE 8082
CMD ["python", "run.py"]

# docker build --pull --rm -f "Dockerfile" -t billing:latest "."
# docker run --rm -d  -p 8082:8082/tcp -h billing_host --net=billing_net billing:latest