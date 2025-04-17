""" This file contains the views for the Ocean Basket app. """
# Import the date class from datetime module
from datetime import date
# Import render, get_object_or_404, and redirect
from django.shortcuts import render, get_object_or_404, redirect
# Import the Booking information model
from .models import BookingInformation
# Import the Booking form
from .forms import BookingForm


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


def edit_booking(request, booking_id):
    """This view handles editing an existing booking."""
    booking_instance = get_object_or_404(BookingInformation, id=booking_id)

    if request.method == 'POST':
        edit_form = BookingForm(request.POST, instance=booking_instance)
        if edit_form.is_valid():
            edit_form.save()
            # Redirect to the bookings page after saving
            return redirect('view_bookings')
    else:
        edit_form = BookingForm(instance=booking_instance)

    context = {
        "edit_form": edit_form
    }
    return render(request, "online_booking/edit_booking.html", context)
