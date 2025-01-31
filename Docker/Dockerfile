# Base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy application code and templates
COPY app.py /app/
COPY templates /app/templates
COPY requirements.txt /app/

# Install dependencies
RUN pip install -r requirements.txt

# Expose the application port
EXPOSE 5000

# Set the entry point
ENTRYPOINT ["python", "app.py"]
