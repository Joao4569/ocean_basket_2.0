"""  This module contains test cases for the BookingInformation model. """
from django.test import TestCase
from .models import BookingInformation


class TestBookingInformationModel(TestCase):
    """Test cases for the BookingInformation model."""

    def test_string_representation(self):
        """Test the string representation of the model."""
        booking = BookingInformation(
            service=BookingInformation.LUNCH,
            username="testuser",
            booking_title="Birthday Party",
            number_of_seats=5,
            date="2023-12-25",
            contact_number="1234567890"
        )
        self.assertEqual(
            str(booking),
            "Birthday Party 1234567890 table for 5 on 2023-12-25"
        )

    def test_field_constraints(self):
        """Test that fields enforce constraints."""
        booking = BookingInformation(
            service=BookingInformation.LUNCH,
            username="testuser",
            booking_title="A" * 51,  # Exceeding max_length
            number_of_seats=5,
            date="2023-12-25",
            contact_number="1234567890"
        )
        with self.assertRaises(Exception):
            booking.full_clean()  # This validates the model fields

    def test_service_choices_validation(self):
        """Test that the service field only accepts valid choices."""
        booking = BookingInformation(
            service="Invalid Choice",
            username="testuser",
            booking_title="Dinner",
            number_of_seats=4,
            date="2023-12-25",
            contact_number="1234567890"
        )
        with self.assertRaises(Exception):
            booking.full_clean()

    def test_model_creation(self):
        """Test that a BookingInformation instance can be created."""
        booking = BookingInformation.objects.create(  # pylint: disable=no-member # noqa: E501
            service=BookingInformation.DINNER,
            username="testuser",
            booking_title="Anniversary Dinner",
            number_of_seats=2,
            date="2023-12-31",
            contact_number="0987654321"
        )
        self.assertEqual(BookingInformation.objects.count(), 1)  # pylint: disable=no-member # noqa: E501
        self.assertEqual(booking.username, "testuser")
