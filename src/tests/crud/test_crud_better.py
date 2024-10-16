# src/tests/crud/test_crud_better.py

import pytest
import requests
from src.helpers.api_request_wrapper import post_request, put_request, delete_request
from src.helpers.payload_manager import get_create_booking_payload, get_update_booking_payload
from src.constants.api_constants import BOOKING_PATH
from src.helpers.common_verification import verify_status_code, verify_booking_data

class TestCreateBooking():

    def test_booking_id(self):
        """Fixture to create a booking and return its ID."""
        headers = {"Content-Type": "application/json"}
        payload = get_create_booking_payload()
        response = post_request(BOOKING_PATH, headers=headers, payload=payload)
        response_data = response.json()
        verify_status_code(response, [200, 201])
        return response_data["bookingid"]


    def test_update_booking(self,auth_token, booking_id):
        """Test case for updating a booking."""
        path = f"{BOOKING_PATH}/{booking_id}"
        cookie = f"token={auth_token}"
        headers = {"Content-Type": "application/json", "Cookie": cookie}
        payload = get_update_booking_payload()

        response = put_request(path, headers=headers, payload=payload)

        response_data = response.json()
        verify_status_code(response, [200])
        # Ensure the response_data is a valid JSON object
        assert isinstance(response_data, dict), f"Invalid response data: {response_data}"

        # Verify the updated booking data
        expected_data = payload
        verify_booking_data(response_data, expected_data)
        print("test_update_booking")


    def test_delete_booking(self,auth_token, booking_id):
        """Test case for deleting a booking."""
        path = f"{BOOKING_PATH}/{booking_id}"
        cookie = f"token={auth_token}"
        headers = {"Content-Type": "application/json", "Cookie": cookie}

        response = delete_request(path, headers=headers)
        try:
            return response.json()  # Try to parse the response as JSON
        except requests.exceptions.JSONDecodeError:
            return response.text  # Return raw response if it's not JSON

        verify_status_code(response, [201, 204])

        # Optionally ensure the response is empty for a successful DELETE
        assert response_data == "", f"Unexpected response data: {response_data}"
        print("3. test_delete_booking")

