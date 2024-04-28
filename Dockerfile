# First stage: Create a virtual environment
FROM python:3.9 AS builder

# Set environment variables
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Second stage: Copy application code and dependencies
FROM python:3.9-slim

# Set environment variables
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Set working directory
WORKDIR /app

# Copy the virtual environment from the previous stage
COPY --from=builder $VIRTUAL_ENV $VIRTUAL_ENV

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

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
