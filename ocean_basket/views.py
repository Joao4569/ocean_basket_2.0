""" This file contains the views for the Ocean Basket app. """
from datetime import date  # Import the date class from datetime module
from django.shortcuts import render
from .models import BookingInformation  # Import the model
from .forms import BookingForm  # Import the form


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


def create_booking(request):  # pylint: disable=W0612
    """ This view renders the create_booking.html template. """
    if request.method == 'POST':
        booking_form = BookingForm(request.POST)
        if booking_form.is_valid():
            booking_form.instance.username = request.user.username
            booking_form.save()
            bookings = BookingInformation.objects.all()  # pylint: disable=no-member # noqa: E501
            context = {
                'bookings': bookings,
            }
            return render(
                request, 'online_booking/view_bookings.html', context
            )
    else:
        booking_form = BookingForm()

    return render(
        request,
        'online_booking/create_booking.html',
        {'booking_form': booking_form}
    )
