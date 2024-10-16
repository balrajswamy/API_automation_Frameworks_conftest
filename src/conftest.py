# src/tests/conftest.py

import pytest
from src.utils.utility import create_token
from src.helpers.api_request_wrapper import post_request
from src.helpers.payload_manager import get_create_booking_payload
from src.constants.api_constants import BOOKING_PATH
from src.helpers.common_verification import verify_status_code


@pytest.fixture(scope="session")
def auth_token():
    """Fixture to get an authentication token for the session."""
    return create_token()

@pytest.fixture(scope="session")
def booking_id():
    """Fixture to create a booking and return its ID."""
    headers = {"Content-Type": "application/json"}
    payload = get_create_booking_payload()
    response = post_request(BOOKING_PATH, headers=headers, payload=payload)
    verify_status_code(response, [200, 201])
    response_data = response.json()
    print("1response_data ", response_data)
    # Ensure the response_data is a valid JSON object
    assert isinstance(response_data, dict), f"Invalid response data: {response_data}"
    return response_data["bookingid"]

