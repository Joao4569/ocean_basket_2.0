# Ocean Basket Restaurant Online Bookings App -  version 2.0

## Introduction

This is a new version of Ocean Basket Restaurant Online Bookings App, this app needed to be updated due to it's version of Django no longer being supported. In this release I will also be updating other software related to this project as well as make use of test driven development (TDD) for the development process.

Version 1.0 can be found in [this repository](https://github.com/Joao4569/ocean-basket-restaurant).

## Table of Contents

* [Project Scope](#Project-Scope)

* [Test Driven Development (TDD)](#Test-Driven-Development)
	* [Testing Django Views](#Testing-Django-Views)
	* [Testing App Configuration](#Testing-App-Configuration)
	* [Coverage](#Coverage)

## Project Scope

In this release I will be doing the following:

 - Django version 3.2.13 will be updated to Version 5.2.
 - I will make use of Python version 3.12.3 instead of 3.9.18.
 - Make use of Docker for containerization.
 - Host the deployed app on Render instead of Heroku.
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

## Coverage

For the use of TDD in this project I installed coverage.py in order to measure test coverage throughout development. When initially installed I made sure that I had 100% coverage on the Ocean Basket app with the goal of maintaining as high a coverage as possible throughout development of the new version of Ocean Basket.
