# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Install system dependencies and Python dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --upgrade pip

# Copy and install Python dependencies
COPY requirements/development.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Copy the project files and the run.sh script
COPY . /app/
RUN chmod +x /app/scripts/run.sh

# Expose the port the app runs on
EXPOSE 8000

# Run the application
CMD ["./scripts/run.sh"]