# Ocean Basket Restaurant Online Bookings App - version 2.0

## Introduction

This is a new version of Ocean Basket Restaurant Online Bookings App, this app needed to be updated due to it's version of Django no longer being supported. In this release I will also be updating other software related to this project as well as make use of test driven development (TDD) for the development process.

Version 1.0 can be found in [this repository](https://github.com/Joao4569/ocean-basket-restaurant).

## Table of Contents

- [Project Scope](#project-scope)

- [Test Driven Development (TDD)](#test-driven-development)

  - [Testing Django Views](#testing-django-views)
    - [Criteria](#test-criteria-for-each-new-view)
  - [Testing App Configuration](#testing-app-configuration)
  - [Coverage](#coverage)

- [Docker](#docker)

  - [Development](#development)
  - [Deployment](#deployment)

- [Access Control](#access-control)
  - [Super User](#super-user)
  - [Store Manager](#store-manager)
  - [Floor Staff](#floor-staff)
  - [Test User](#test-user)

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

1. **HTTP Response Status Code**: Test that the HTTP response status code for the view is 200, which means the page loaded successfully without errors. If the status code is not 200, the test will fail.

2. **Template Rendering**: Test that the correct template is used when rendering the view. If a different template is used or no template is used at all, the test will fail.

3. **User Authentication**: For views that require user authentication, tests ensure that only authenticated users can access the view. If an unauthenticated user attempts to access the view, the test will check for a redirect to the login page.

4. **Form Handling**: For views that involve forms (e.g., creating or editing bookings), tests verify that valid form submissions result in the expected changes to the database and that invalid submissions return appropriate error messages.

5. **Redirects**: For views that involve actions like login, signup, or deleting a booking, tests ensure that the user is redirected to the correct page after the action is completed.

6. **Database Integrity**: Tests verify that the database reflects the expected state after actions like creating, editing, or deleting bookings.

By following these criteria, I ensure that each view is thoroughly tested for functionality, user experience, and security. This approach demonstrates my commitment to quality and attention to detail in the development process.

### Testing App Configuration

The `test_app_config.py` file contains a unit test to verify the configuration of the `ocean_basket` app. This test ensures that the app is correctly registered and configured within the Django project.

#### How App Configuration is Tested

1. **App Name Verification**: The test checks that the `name` attribute of the `OceanBasketConfig` class matches the expected app name, `ocean_basket`. This ensures that the app's configuration is correctly defined in the `apps.py` file.

2. **Django App Registry**: The test verifies that the app is properly registered in Django's app registry by comparing the app name retrieved from the registry with the expected app name. This ensures that the app is correctly recognized by the Django framework.

By including these tests, I ensure that the foundational configuration of the `ocean_basket` app is accurate and reliable. This demonstrates my attention to detail and commitment to maintaining a robust and well-structured application.

### Coverage

For the use of TDD in this project I installed coverage.py in order to measure test coverage throughout development. When initially installed I made sure that I had 100% coverage on the Ocean Basket app with the goal of maintaining as high a coverage as possible throughout development of the new version of Ocean Basket.

## Docker

### Development

For development purposes, Docker is used to containerize the application, ensuring consistency across different environments. The `docker-compose.yml` file defines the services required for the application, including the app service. The app service uses a custom Docker image built from the `Dockerfile`. The following resources are utilized:

- **Dockerfile**: Defines the base image, dependencies, and commands to set up the application environment.
- **docker-compose.yml**: Simplifies the process of running the application by managing the container's configuration, such as port mapping and volume mounting.
- **Volumes**: The current directory is mounted into the container to allow real-time updates during development.

To start the application in a development environment with a new image, use the following command:

```powershell
docker compose up -d --build
```

As a best practice I clear the cache whenever significant changes have been made by using the following command:

```powershell
docker system prune
```

### Deployment

For deployment, the Docker image is built and pushed to GitHub Packages. This image is then used by Render to host the application. The deployment process involves the following steps:

1. **Build the Docker Image**: The Docker image is built locally using the `Dockerfile`.
2. **Push to GitHub Packages**: The built image is pushed to GitHub Packages using a Personal Access Token (PAT) for authentication. This ensures secure read and write access for Render.
3. **Render Integration**: Render pulls the Docker image from GitHub Packages and uses it to deploy the application.

This process is currently manual, requiring the image to be rebuilt and pushed for every new change. Automation of this workflow is planned for future iterations.

To push the image to GitHub Packages, use the following commands:

```powershell
docker build -t ghcr.io/joao4569/ocean-basket-app-image .
docker push ghcr.io/joao4569/ocean-basket-app-image:latest
```

Ensure that the Personal Access Token is configured in your Docker CLI for authentication with GitHub Packages.

## Access Control

I have created a few users which will be helpful for testing the project:

### Super User

I created a Superuser in order to access the admin functions of Django. The Superuser is also what I use to create employees, as it is now a new employee can register his or her self the same way as a customer and with the Superuser logged in, one can allocate the "is Staff" property on the admin site.

Credentials:

- Username: **SuperUserProd**
- Password: **OceanBasketSuperProd4569**

### Store Manager

This store manager I created is a universal store manager user which can access more detailed information for the current days bookings via the application in order to be able to access customers contact details if needed for managerial purposes. This username can be allocated a new password if a new store manager is employed, this allocation must be done by the superuser.

Credentials:

- Username: **StoreManager**
- Password: **Peter4569**

### Floor Staff

This employee I created is a universal position for any floor staff which can access basic information for the current days bookings via the application in order to plan for the days services and group numbers.

Credentials:

- Username: **FloorStaff**
- Password: **OceanBasketStaff**

### Test User

These are the credentials for a User that I created for testing:

Credentials:

- Username: **TestUser**
- Password: **OceanBasketUser**
