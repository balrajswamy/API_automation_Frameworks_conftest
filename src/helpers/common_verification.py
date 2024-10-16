# helpers/common_verification.py

def verify_status_code(response, expected_status_codes):
    """Verify the response status code."""
    assert response.status_code in expected_status_codes, f"Unexpected status code: {response.status_code}"

def verify_booking_data(response_data, expected_data):
    """Verify that the response data matches the expected data."""
    for key, value in expected_data.items():
        assert response_data.get(key) == value, f"Mismatch in {key}: expected {value}, got {response_data.get(key)}"
