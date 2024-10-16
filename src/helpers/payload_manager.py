# helpers/payload_manager.py

def get_create_booking_payload():
    """Return a payload for creating a booking."""
    return {
        "firstname": "Balraj",
        "lastname": "Ponnuswamy",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-10-10",
            "checkout": "2024-10-11"
        },
        "additionalneeds": "Breakfast"
    }

def get_update_booking_payload():
    """Return a payload for updating a booking."""
    return {
        "firstname": "Balraj",
        "lastname": "Balaji",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-10-10",
            "checkout": "2024-10-11"
        },
        "additionalneeds": "Breakfast"
    }

def get_auth_payload():
    """Return a payload for authentication."""
    return {
        "username": "admin",
        "password": "password123"
    }
