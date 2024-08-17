import allure
import pytest


class TestCreateBooking(object):
    @pytest.mark.positive
    @allure.title("Verify that create Booking status and booking ID should not be null")
    @allure.description(
        "Creating a booking from payload and verify that booking is should not be null"
    )
    def test_create_booking_positive(self):
        pass
