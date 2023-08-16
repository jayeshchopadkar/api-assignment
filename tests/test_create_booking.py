from utils.api_helpers import APIHelpers


def test_create_booking():
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

    response = APIHelpers.create_booking(data)

    assert response.status_code == 200, "Create booking failed"
