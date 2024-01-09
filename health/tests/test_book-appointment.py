import unittest
from datetime import datetime, timedelta


class AppointmentScheduler:
    def __init__(self):
        self.appointments = []

    def book_appointment(self, appointment_time):
        # Assume appointments are booked for a duration of 1 hour
        end_time = appointment_time + timedelta(hours=1)

        # Check if the proposed time slot is available
        if all(
            end_time <= appointment["start_time"] or appointment_time >= appointment["end_time"]
            for appointment in self.appointments
        ):
            self.appointments.append({"start_time": appointment_time, "end_time": end_time})
            return True
        else:
            return False


class TestAppointmentScheduler(unittest.TestCase):

    def test_book_appointment_next_two_weeks(self):
        scheduler = AppointmentScheduler()
        current_time = datetime.now()
        appointment_time = current_time + timedelta(weeks=2)

        result = scheduler.book_appointment(appointment_time)

        self.assertTrue(result, f"Booking appointment at {appointment_time} should succeed")
        self.assertEqual(len(scheduler.appointments), 1, "There should be one appointment booked")


if __name__ == '__main__':
    unittest.main()
