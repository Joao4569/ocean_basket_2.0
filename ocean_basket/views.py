""" This file contains the views for the Ocean Basket app. """
from datetime import date  # Import the date class from datetime module
from django.shortcuts import render
from .models import BookingInformation  # Import the model


def home(request):
    """ This view renders the index.html template. """
    return render(request, 'online_booking/index.html')


def view_bookings(request):
    """ This view renders the view_booking.html template. """
    bookings = BookingInformation.objects.all()  # pylint: disable=no-member
    context = {
        'bookings': bookings,
    }
    return render(request, 'online_booking/view_bookings.html', context)


def view_bookings_employee(request):
    """ This view renders the booking.html template for
    Ocean Basket employees. """
    today = date.today()  # noqa: F841  # pylint: disable=W0612
    bookings = BookingInformation.objects.all()  # pylint: disable=no-member
    context = {
        'bookings': bookings,
    }
    return render(request, 'online_booking/view_bookings.html', context)
