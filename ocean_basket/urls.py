""" This is the URL configuration for the ocean_basket app.
It maps URLs to views. """
from django.urls import path
from . import views


urlpatterns = [
    # URL pattern for index.html
    path('', views.home, name='Home'),
    # URL pattern for view_bookings.html
    path('view_bookings/', views.view_bookings, name='View your bookings'),
    # URL pattern for view_bookings_employee.html
    path(
            'view_bookings_employee/',
            views.view_bookings_employee,
            name='View days bookings'
        ),

]
