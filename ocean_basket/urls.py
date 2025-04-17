""" This is the URL configuration for the ocean_basket app.
It maps URLs to views. """
from django.urls import path
from . import views


urlpatterns = [
    # URL pattern for index.html
    path('', views.home, name='Home'),
    # URL pattern for view_bookings.html
    path('view_bookings/', views.view_bookings, name='view_bookings'),
    # URL pattern for view_bookings_employee.html
    path(
            'view_bookings_employee/',
            views.view_bookings_employee,
            name='View days bookings'
        ),
    # URL pattern for create_booking.html
    path('create_booking/', views.create_booking, name='Create booking'),
    # URL pattern for edit_booking.html
    path(
            'edit_booking/<int:booking_id>/',
            views.edit_booking,
            name='Edit booking'
        ),
    # URL pattern for delete_booking.html
    path(
            'delete_booking/<int:booking_id>/',
            views.delete_booking,
            name='Delete booking'
        ),
]
