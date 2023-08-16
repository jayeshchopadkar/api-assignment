import pytest
from utils.api_helpers import APIHelpers


def test_update_booking():
    # Create a booking to update its details
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

    # Update booking details
    updated_data = {
        "firstname": "UpdatedJayesh",
        "lastname": "UpdatedChopadkar",
        "totalprice": 150,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2023-08-18",
            "checkout": "2023-08-22"
        },
        "additionalneeds": "Lunch"
    }
    response = APIHelpers.update_booking(booking_id, updated_data)

    assert response.status_code == 403, "Update booking failed"
    # Add more assertions based on the API response content as needed
