import requests


class APIHelpers:
    BASE_URL = "https://restful-booker.herokuapp.com"

    @staticmethod
    def create_booking(data):
        url = f"{APIHelpers.BASE_URL}/booking"
        response = requests.post(url, json=data)
        return response

    @staticmethod
    def get_booking(booking_id):
        url = f"{APIHelpers.BASE_URL}/booking/{booking_id}"
        response = requests.get(url)
        return response

    @staticmethod
    def update_booking(booking_id, data):
        url = f"{APIHelpers.BASE_URL}/booking/{booking_id}"
        response = requests.put(url, json=data)
        return response

    @staticmethod
    def delete_booking(booking_id):
        url = f"{APIHelpers.BASE_URL}/booking/{booking_id}"
        response = requests.delete(url)
        return response
