#!/bin/bash

# Wait for 4 seconds after MySQL container is launched
echo "Waiting for MySQL container to be ready..."
sleep 4

# Apply database migrations
python trafficviolation/manage.py migrate

# Create a superuser if it doesn't already exist
# echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python trafficviolation/manage.py shell
echo "user is staff"
# Grant staff status to the superuser
echo "from django.contrib.auth.models import User; user = User.objects.get(username='admin'); user.is_staff = True; user.save()" | python trafficviolation/manage.py shell

echo "exec gunicorn"
# Start Django development server
gunicorn trafficviolation.trafficviolation.wsgi:application --bind 0.0.0.0:8000
