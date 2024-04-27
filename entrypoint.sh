#!/bin/bash

# Apply database migrations
python manage.py migrate

# Grant staff status to the superuser
echo "from django.contrib.auth.models import User; user = User.objects.get(username='admin'); user.is_staff = True; user.save()" | python manage.py shell

# Start Django development server
python manage.py runserver 0.0.0.0:8000
