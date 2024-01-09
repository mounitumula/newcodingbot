import unittest
import re


def is_valid_email(email):
    # Regular expression for a basic email validation
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None


class TestEmailValidation(unittest.TestCase):

    def test_valid_emails(self):
        valid_emails = [
            'user@example.com',
            'john.doe123@gmail.com',
            'test.email@domain.co.uk',
            'info@company.net'
        ]

        for email in valid_emails:
            with self.subTest(email=email):
                self.assertTrue(is_valid_email(email), f"{email} should be valid")

    def test_invalid_emails(self):
        invalid_emails = [
            'invalid-email',
            'user@.com',
            '@missing-username.com',
            'user@invalid@domain.com'
        ]

        for email in invalid_emails:
            with self.subTest(email=email):
                self.assertFalse(is_valid_email(email), f"{email} should be invalid")


if __name__ == '__main__':
    unittest.main()
