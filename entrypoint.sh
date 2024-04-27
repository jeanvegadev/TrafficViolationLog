#!/bin/bash

# Apply database migrations
python trafficviolation/manage.py migrate

# Create a superuser if it doesn't already exist
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell

# Grant staff status to the superuser
echo "from django.contrib.auth.models import User; user = User.objects.get(username='admin'); user.is_staff = True; user.save()" | python trafficviolation/manage.py shell

# Start Django development server
gunicorn trafficviolation.trafficviolation.wsgi:application --bind 0.0.0.0:8000
