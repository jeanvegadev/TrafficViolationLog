FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Create and activate the virtual environment
ENV VIRTUAL_ENV=/app/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy the entrypoint script into the container
COPY entrypoint.sh /app/

# Make the entrypoint script executable
RUN chmod +x /app/entrypoint.sh

# Copy the Django project into the container
COPY . /app/

# Set the entrypoint
ENTRYPOINT ["/app/entrypoint.sh"]
