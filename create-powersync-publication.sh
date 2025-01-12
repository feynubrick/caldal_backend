#!/bin/bash
set -e
export PGPASSWORD="$DATABASE_PASSWORD"
psql -v ON_ERROR_STOP=1 \
    --host "$DATABASE_HOST" \
    --dbname "$DATABASE_NAME" \
    --username "$DATABASE_USER" \
    <<- EOSQL
    CREATE PUBLICATION powersync FOR ALL TABLES;
EOSQL
