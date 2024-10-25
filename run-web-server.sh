#!/bin/bash

if [ "$RUN_ENV" = "prod" ]; then
  cp deploy/"$RUN_ENV".nginx /etc/nginx/sites-available/default
  echo "Starting nginx with deploy/$RUN_ENV.nginx..."
  service nginx start
  echo "nginx started!"

  echo "Running migrate..."
  python manage.py migrate --no-input
  echo "migrate finished!"
fi

echo "Running collectstatic..."
python manage.py collectstatic --no-input
echo "collectstatic finished!"

if [ "$RUN_ENV" = "prod" ]; then
    echo "Starting in PROD mode..."

    # workers = ($num_core X 2) + 1
    echo "Running gunicorn..."
    gunicorn \
      --access-logformat '%(h)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'\
      --access-logfile - \
      --error-logfile - \
      --capture-output \
      --log-level info \
      --workers 5 \
      --bind 127.0.0.1:8000 \
      --max-requests 1000 \
      --max-requests-jitter 50 \
      --worker-class uvicorn.workers.UvicornWorker \
      caldal.config.asgi:application

else
    echo "Staring in LOCAL mode..."

    # python manage.py migrate
    echo "Running runserver_plus..."
    python manage.py runserver 0.0.0.0:8000
fi
