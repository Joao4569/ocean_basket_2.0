""" This module is used to register the BookingInformation model with the
Django admin site. """
from django.contrib import admin
from .models import BookingInformation


admin.site.register(BookingInformation)
