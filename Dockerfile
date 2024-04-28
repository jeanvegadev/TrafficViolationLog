FROM python:3.9.19-alpine3.19

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Create and activate the virtual environment
RUN python -m venv venv
ENV VIRTUAL_ENV=/app/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies
COPY requirements.txt /app/
RUN /app/venv/bin/pip install --no-cache-dir -r requirements.txt

# Copy the entrypoint script into the container
COPY entrypoint.sh /app/

# Make the entrypoint script executable
RUN chmod +x /app/entrypoint.sh

# Copy the Django project into the container
COPY . /app/

# Set the entrypoint
ENTRYPOINT ["/app/entrypoint.sh"]

# Set the command to run your application
CMD ["gunicorn", "trafficviolation.trafficviolation.wsgi:application", "--bind", "0.0.0.0:8000"]
