# utils/utility.py

from src.helpers.api_request_wrapper import post_request
from src.helpers.payload_manager import get_auth_payload
from src.constants.api_constants import AUTH_PATH

def create_token():
    """Create an authentication token."""
    headers = {"Content-Type": "application/json"}
    payload = get_auth_payload()
    response = post_request(AUTH_PATH, headers=headers, payload=payload)
    response_data = response.json()
    return response_data.get("token")
