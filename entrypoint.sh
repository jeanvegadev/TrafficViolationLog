#!/bin/bash

# Function to check if MySQL container is ready
wait_for_mysql() {
    local host=db
    local port=3306
    local delay=1
    local max_retries=30

    echo "Waiting for MySQL container to be ready..."
    for ((i=0; i<$max_retries; i++)); do
        if command -v ncat >/dev/null; then
            if ncat -z "$host" "$port"; then
                echo "MySQL container is ready."
                return 0
            fi
        elif command -v curl >/dev/null; then
            if curl -s "$host:$port" | grep -q "MySQL"; then
                echo "MySQL container is ready."
                return 0
            fi
        elif command -v wget >/dev/null; then
            if wget -qO- "$host:$port" | grep -q "MySQL"; then
                echo "MySQL container is ready."
                return 0
            fi
        fi
        sleep "$delay"
    done

    echo "Timeout: MySQL container did not become ready after $((delay * max_retries)) seconds."
    exit 1
}

# Apply database migrations
python trafficviolation/manage.py migrate

# Create a superuser if it doesn't already exist
# echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python trafficviolation/manage.py shell

# Grant staff status to the superuser
echo "from django.contrib.auth.models import User; user = User.objects.get(username='admin'); user.is_staff = True; user.save()" | python trafficviolation/manage.py shell

# Start Django development server
# gunicorn trafficviolation.trafficviolation.wsgi:application --bind 0.0.0.0:8000
