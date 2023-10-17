# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app


# Install a suitable C compiler (in this case, gcc)
RUN apt-get update && apt-get install -y build-essential

# Copy the Pipfile and Pipfile.lock into the container at /app
COPY Pipfile Pipfile.lock /app/

# Install Pipenv
RUN pip install pipenv

# Install dependencies using Pipenv
RUN pipenv install --system --deploy

# Copy the current directory contents into the container at /app
COPY . /app

# Expose the port that the app runs on
EXPOSE 8000


# Start FastAPI app and Celery worker when the container launches
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port 8000"]
