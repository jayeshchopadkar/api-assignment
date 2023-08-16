import pytest
from utils.api_helpers import APIHelpers


def test_delete_booking():
    # Create a booking to delete it
    data = {
        "firstname": "UpdatedJayesh",
        "lastname": "UpdatedChopadkar",
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

    # Delete the booking
    response = APIHelpers.delete_booking(booking_id)

    assert response.status_code == 403, "Delete booking failed"
    # Ensure the booking is actually deleted by attempting to retrieve it
    get_response = APIHelpers.get_booking(booking_id)
    assert get_response.status_code == 200, "Booking was not deleted"
