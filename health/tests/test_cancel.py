import unittest
from datetime import datetime, timedelta


class AppointmentScheduler:
    def __init__(self):
        self.appointments = []

    def book_appointment(self, appointment_time, person, appointments=[]):
        # Assume appointments are booked for a duration of 1 hour
        end_time = appointment_time + timedelta(hours=1)

        # Check if the proposed time slot is available
        if all(
            end_time <= appointment["start_time"] or appointment_time >= appointment["end_time"]
            for appointment in self.appointments
        ):

            self.appointments.append({"start_time": appointment_time, "end_time": end_time, "person": person,
                                      "count": 0})
            return True
        else:
            return False

    def cancel_appointment(self, appointment_time, person, appointments=[]):
        # Remove the appointment matching the given time and person
        if appointments:
            for index, i in enumerate(appointments):
                if i.get("person") == person:
                    # check if count is greater than 2
                    if i.get("count") >= 2:
                        return False
                    else:
                        self.appointments.pop(0)
                        i["count"] = i["count"] + 1
                        appointments[index] = i
                else:
                    continue
        else:
            # remove booking from list
            self.appointments.pop(0)
            # this is the first appointment
            appointments.append({"cancelled": True, "count": 1, "person": person})
        return appointments


class TestAppointmentScheduler(unittest.TestCase):

    def test_cancel_only_two_appointments_for_same_person_in_a_month(self):
        scheduler = AppointmentScheduler()
        appointments = []
        # Book three appointments for the same person
        appointment_time_1 = datetime(2024, 1, 15, 10, 0)
        scheduler.book_appointment(appointment_time_1, "John Doe", appointments)
        appointments = scheduler.cancel_appointment(appointment_time_1, "John Doe", appointments)

        appointment_time_2 = datetime(2024, 1, 20, 14, 0)
        scheduler.book_appointment(appointment_time_2, "John Doe")
        appointments = scheduler.cancel_appointment(appointment_time_2, "John Doe", appointments)

        appointment_time_3 = datetime(2024, 1, 25, 16, 0)
        scheduler.book_appointment(appointment_time_3, "John Doe")
        appointments = scheduler.cancel_appointment(appointment_time_2, "John Doe", appointments)

        if isinstance(appointments, bool):
            if not appointments:
                # cancellation limit exceeded for month, there should be one booking left for that person
                self.assertEqual(len(scheduler.appointments), 1, "There should be one appointment remaining")
                # Ensure the third appointment is still in the list for the same person
                remaining_appointment = scheduler.appointments[0]
                self.assertEqual(remaining_appointment["start_time"], appointment_time_3,
                                 "The third appointment should still be present")
                self.assertEqual(remaining_appointment["person"], "John Doe",
                                 "The appointment should still be for the same person")


if __name__ == '__main__':
    unittest.main()
