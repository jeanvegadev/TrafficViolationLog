#!/bin/bash

# Apply database migrations
python trafficviolation/manage.py migrate

# Grant staff status to the superuser
echo "from django.contrib.auth.models import User; user = User.objects.get(username='admin'); user.is_staff = True; user.save()" | python trafficviolation/manage.py shell

# Start Django development server
gunicorn trafficviolation/trafficviolation/wsgi:application --bind 0.0.0.0:8000
