""" This file contains the views for the Ocean Basket app. """
from django.shortcuts import render
from .models import BookingInformation  # Import the model


def home(request):
    """ This view renders the index.html template. """
    return render(request, 'online_booking/index.html')


def view_bookings(request):
    """ This view renders the booking.html template. """
    bookings = BookingInformation.objects.all()  # pylint: disable=no-member
    context = {
        'bookings': bookings,
    }
    return render(request, 'online_booking/view_bookings.html', context)
