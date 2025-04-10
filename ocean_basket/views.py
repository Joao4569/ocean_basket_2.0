""" This file contains the views for the Ocean Basket app. """
from django.shortcuts import render


def home(request):
    """ This view renders the index.html template. """
    return render(request, 'online_booking/index.html')
