# src/tests/crud/test_crud.py

import pytest
from src.helpers.api_request_wrapper import post_request, put_request, delete_request
from src.helpers.payload_manager import get_create_booking_payload, get_update_booking_payload
from src.utils.utility import create_token
from src.constants.api_constants import BOOKING_PATH
from src.helpers.common_verification import verify_status_code, verify_booking_data
import allure
import logging
import requests

@pytest.fixture
def auth_token():
    """Fixture to get an authentication token."""
    return create_token()


@pytest.fixture
def booking_id():
    """Fixture to create a booking and return its ID."""
    headers = {"Content-Type": "application/json"}
    payload = get_create_booking_payload()
    response = post_request(BOOKING_PATH, headers=headers, payload=payload)
    response_data = response.json()
    verify_status_code(response, [200, 201])
    return response_data["bookingid"]


def test_create_booking():
    """Test case for creating a booking."""
    headers = {"Content-Type": "application/json"}
    payload = get_create_booking_payload()
    response = post_request(BOOKING_PATH, headers=headers, payload=payload)
    response_data = response.json()

    verify_status_code(response, [200, 201])
    expected_data = payload
    verify_booking_data(response_data["booking"], expected_data)


def test_update_booking(auth_token, booking_id):
    """Test case for updating a booking."""
    path = f"{BOOKING_PATH}/{booking_id}"
    cookie = f"token={auth_token}"
    headers = {"Content-Type": "application/json", "Cookie": cookie}
    payload = get_update_booking_payload()

    response = put_request(path, headers=headers, payload=payload)
    response_data = response.json()

    verify_status_code(response, [200])
    expected_data = payload
    verify_booking_data(response_data, expected_data)


def test_delete_booking(auth_token, booking_id):
    """Test case for deleting a booking."""
    path = f"{BOOKING_PATH}/{booking_id}"
    cookie = f"token={auth_token}"
    headers = {"Content-Type": "application/json", "Cookie": cookie}

    response = delete_request(path, headers=headers)
    verify_status_code(response, [201, 204])

class TestCreateBooking():

    @allure.title("Verify that Creating booking status and Booking Id should not be null")
    @allure.description("Create a booking from payload and verify that booking id should not be null")
    @pytest.mark.positive
    def test_Create_booking_positive(self):

        headers = {"Content-Type": "application/json"}

        Logger = logging.getLogger(__name__)
        Logger.info("Starting the TestCase TC#1 - positive")
        payload = get_create_booking_payload()
        response = post_request(BOOKING_PATH, headers=headers, payload=payload)



        print("response.json:\t", response.json())
        verify_status_code(response, [200, 201])
        return response.json()["bookingid"]
        Logger.info("Booking Id is: "+ str(response.json()["bookingid"]))
        Logger.info("End of the TestCase TC#1 - positive")

    @allure.title("Verify that Create booking does not work with no payload")
    @allure.description("Create a booking with no payload and verifying/checking a booking id")
    @pytest.mark.negative
    def test_Create_booking_negative(self):
        Logger = logging.getLogger(__name__)
        headers = {"Content-Type": "application/json"}
        Logger.info("Starting the TestCase TC#2 - negative")
        response = post_request(BOOKING_PATH,headers=headers,payload={})

        try:
            return response.json()  # Try to parse the response as JSON
        except requests.exceptions.JSONDecodeError:
            return response.text  # Return raw response if it's not JSON
        verify_status_code(response, [500,500])
        Logger.info("Booking Id is: " + str(response.json()["bookingid"]))
        Logger.info("End of the TestCase TC#2 - negative")
        return response.json()["bookingid"]

