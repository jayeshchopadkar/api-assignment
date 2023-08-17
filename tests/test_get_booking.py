import pytest
import logging
from utils.api_helpers import APIHelpers


def test_get_booking():
    # Create a booking to get its ID for testing
    data = {
        "firstname": "Jayesh",
        "lastname": "Chopadkar",
        "totalprice": 100,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-08-16",
            "checkout": "2023-08-20"
        },
        "additionalneeds": "Breakfast"
    }
    create_response = APIHelpers.create_booking(data)
    booking_id = create_response.json()["bookingid"]

    # Test the Get Booking API
    response = APIHelpers.get_booking(booking_id)

    assert response.status_code == 200, "Get booking failed"
    # Add more assertions based on the API response content as needed
