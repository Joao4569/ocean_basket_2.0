""" This is the URL configuration for the ocean_basket app.
It maps URLs to views. """
from django.urls import path
from . import views


urlpatterns = [
    # URL pattern for index.html
    path('', views.home, name='home'),
    # URL pattern for bookings.html
    path('view_bookings/', views.view_bookings, name='view_bookings'),
]
