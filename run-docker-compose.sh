#!/bin/bash

export TZ=Asia/Seoul
current_time=$(date "+%Y-%m-%d_%H-%M-%S")
export LOG_STREAM_NAME="$current_time"

if [ -z "$1" ]; then
  echo "No service name provided. Running all services."
  service_name=""
else
  echo "Service name provided: $1"
  service_name="$1"
fi


if [ "$RUN_ENV" == "prod" ]; then
  echo "run docker compose for PROD"

  docker compose \
    -f compose.prod.yaml \
    -p caldal-backend-prod \
    --env-file prod.env \
    up \
    --force-recreate \
    --build \
    --remove-orphans \
    -d $service_name

else
  echo "run docker compose for LOCAL"
  echo "$service_name"

  docker compose \
    -f compose.local.yaml \
    -p caldal-backend-local \
    --env-file local.env \
    up \
    --force-recreate \
    --build \
    --remove-orphans \
    -d $service_name
fi
