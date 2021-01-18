# Include a slim python environment
FROM python:3.6-slim

# Copy the current directory at host to /app of container
COPY . /app

# Set the working directory to /app
WORKDIR /app

# Install the python dependencies
RUN pip install -r requirements.txt

# Command for running python app
CMD ["python", "app/index.py"]