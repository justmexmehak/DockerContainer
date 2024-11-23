# Use Python as the base image
FROM python:3.9-slim

# Install Flask for the web server
RUN pip install flask pyjokes

# Add the app
COPY app.py /app.py

# Run the app
CMD ["python", "/app.py"]
