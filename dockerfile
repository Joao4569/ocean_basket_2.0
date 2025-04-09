FROM python:3.12.10-slim-bookworm

# This environment variable is used to prevent Python from writing .pyc files to disk.
ENV PYTHONDONTWRITEBYTECODE=1

# This environment variable is used to ensure that Python output is sent straight to terminal (e.g. for Docker logs).
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container to /app
WORKDIR /ocean-basket-app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install the latest version of pip
RUN pip install --upgrade pip

# Install the required packages for the application
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Collect static files for the Django application
# This command collects all static files from the Django app and places them in the STATIC_ROOT directory.
RUN python manage.py collectstatic --noinput

# Expose port 8000 for the application
EXPOSE 8000

# Command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
