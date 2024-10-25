FROM python:3.12.7-bookworm

RUN apt update -y && apt install -y libpq-dev python3-dev nginx build-essential

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

COPY . .

# Link Nginx logs to Docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

ENTRYPOINT ["bash", "./run-web-server.sh"]
