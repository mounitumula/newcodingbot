import unittest
import re


def is_valid_indian_phone_number(phone_number):
    # Regular expression for a basic Indian phone number validation
    # This example assumes common formats: +91 XXXXXXXXXX, 0XXXXXXXXXX, or 0XX-XXXXXXXX
    pattern = r'^(?:\+91|0)?(?:\d{10}|0\d{10}|0\d{2}-\d{8})$'
    return re.match(pattern, phone_number) is not None


class TestIndianPhoneNumberValidation(unittest.TestCase):

    def test_valid_indian_phone_numbers(self):
        valid_phone_numbers = [
            '+91 1234567890',
            '09876543210',
            '01234-567890',
            '09123456789'
        ]

        for phone_number in valid_phone_numbers:
            with self.subTest(phone_number=phone_number):
                self.assertTrue(is_valid_indian_phone_number(phone_number), f"{phone_number} should be valid")

    def test_invalid_indian_phone_numbers(self):
        invalid_phone_numbers = [
            '123-45-67890',     # Invalid format
            '987654321',        # Invalid format
            '+91 123456789',    # Invalid format
            '0123-45678901'     # Invalid format
        ]

        for phone_number in invalid_phone_numbers:
            with self.subTest(phone_number=phone_number):
                self.assertFalse(is_valid_indian_phone_number(phone_number), f"{phone_number} should be invalid")

if __name__ == '__main__':
    unittest.main()
