# Ocean Basket Restaurant Online Bookings App - version 2.0

## Introduction

This is a new version of Ocean Basket Restaurant Online Bookings App, this app needed to be updated due to it's version of Django no longer being supported. In this release I will also be updating other software related to this project as well as make use of test driven development (TDD) for the development process.

Version 1.0 can be found in [this repository](https://github.com/Joao4569/ocean-basket-restaurant).

## Table of Contents

- [Project Scope](#Project-Scope)

- [Test Driven Development (TDD)](#Test-Driven-Development)

  - [Testing Django Views](#Testing-Django-Views)
  - [Testing App Configuration](#Testing-App-Configuration)
  - [Coverage](#Coverage)

- [Docker](#Docker)

## Project Scope

In this release I will be doing the following:

- Django version 3.2.13 will be updated to Version 5.2.
- I will make use of Python version 3.12.10 instead of 3.9.18.
- Upgrade all dependencies.
- Make use of Docker for containerization.
- Host the deployed app and database on Render instead of Heroku.
- Make use of [TDD Test Driven Development](#Test-Driven-Development) for the construction of this version.

## Test Driven Development

I am making use of TDD for the construction of this new version. Here is how I plan to do so:

### Testing Django Views

Prior to constructing each view on Django, I will first create a test for that view which will initially fail as the view will not exist yet. After I have created the view then the test should pass, this process will be repeated for each new view created.

#### Test criteria for each new view

Each new view will have a test created which will test for the following:

1. Test that the HTTP response status code for the view is 200, which means the page loaded successfully without errors. If the status code is not 200, the test will fail.

2. Test that the correct template is used when rendering the view. If a different template is used or no template is used at all, the test will fail.

### Testing App Configuration

The `test_app_config.py` file contains a unit test to verify the configuration of the `ocean_basket` app. This test ensures that the app is correctly registered and configured within the Django project.

### Coverage

For the use of TDD in this project I installed coverage.py in order to measure test coverage throughout development. When initially installed I made sure that I had 100% coverage on the Ocean Basket app with the goal of maintaining as high a coverage as possible throughout development of the new version of Ocean Basket.

## Docker

### Development

For development purposes, Docker is used to containerize the application, ensuring consistency across different environments. The `docker-compose.yml` file defines the services required for the application, including the app service. The app service uses a custom Docker image built from the `Dockerfile`. The following resources are utilized:

- **Dockerfile**: Defines the base image, dependencies, and commands to set up the application environment.
- **docker-compose.yml**: Simplifies the process of running the application by managing the container's configuration, such as port mapping and volume mounting.
- **Volumes**: The current directory is mounted into the container to allow real-time updates during development.

To start the application in a development environment, use the following command:

```bash
docker-compose up -d
```

### Deployment

For deployment, the Docker image is built and pushed to GitHub Packages. This image is then used by Render to host the application. The deployment process involves the following steps:

1. **Build the Docker Image**: The Docker image is built locally using the `Dockerfile`.
2. **Push to GitHub Packages**: The built image is pushed to GitHub Packages using a Personal Access Token (PAT) for authentication. This ensures secure read and write access for Render.
3. **Render Integration**: Render pulls the Docker image from GitHub Packages and uses it to deploy the application.

This process is currently manual, requiring the image to be rebuilt and pushed for every new change. Automation of this workflow is planned for future iterations.

To push the image to GitHub Packages, use the following commands:

```bash
docker build -t ghcr.io/<joao4569>/ocean-basket-app:latest .
docker push ghcr.io/<joao4569>/ocean-basket-app:latest
```

Ensure that the Personal Access Token is configured in your Docker CLI for authentication with GitHub Packages.
