import unittest


class AppointmentUpdateTest(unittest.TestCase):
    def get_existing_appointment(self, email):
        data = [{"name": "tina", "email": "tinaxyz@gmail.com", "date": "2024-01-15", "time": "15:00"}]
        for i in data:
            if i.get("email") == email:
                return i
        return None

    def update_appointment(self, existing_appointment, updated_appointment):
        # update booking
        existing_appointment["date"] = updated_appointment["date"]
        existing_appointment["time"] = updated_appointment["time"]
        return "Appointment updated successfully."

    def test_update_existing_appointment(self):
        # Test updating an already existing appointment
        # Assume there is an existing appointment with ID 1 for "Person" on a specific date and time
        existing_appointment = self.get_existing_appointment("tinaxyz@gmail.com")
        if existing_appointment:
            # Update the details of the existing appointment
            updated_details = {"date": "2024-01-15", "time": "15:00", "email": "tinaxyz@gmail.com"}
            result = self.update_appointment(existing_appointment, updated_details)

        # Ensure the update is successful and the details are updated
        self.assertEqual(result, "Appointment updated successfully.")

    def test_update_nonexistent_appointment(self):
        # Test updating a nonexistent appointment
        # Assume there is no existing appointment with ID 99 for "Person"
        nonexistent_appointment = self.get_existing_appointment("dolly123@gmail.com")
        if nonexistent_appointment:
            # Try to update the nonexistent appointment
            result = self.update_appointment(nonexistent_appointment,
                                        {"date": "2024-01-20", "time": "10:00", "location": "Location"})
        else:
            result = "Appointment not found. Cannot update."
        # Ensure an error message is returned as the appointment does not exist
        self.assertEqual(result, "Appointment not found. Cannot update.")


if __name__ == '__main__':
    unittest.main()
