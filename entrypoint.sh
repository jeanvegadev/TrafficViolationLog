#!/bin/bash

# Wait for 4 seconds after MySQL container is launched
echo "Waiting for MySQL container to be ready..."
python manage.py wait_for_db

echo "collect statics"
python manage.py collectstatic --no-input

# Apply database migrations
python manage.py migrate

echo "user is staff"
# Grant staff status to the superuser
echo "from django.contrib.auth.models import User; user = User.objects.get(username='admin'); user.is_staff = True; user.save()" | python manage.py shell

echo "exec gunicorn"
# Start Django development server
gunicorn trafficviolation.wsgi:application --bind 0.0.0.0:8000
