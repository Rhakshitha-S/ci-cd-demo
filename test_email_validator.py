import unittest
from email_validator import is_valid_email

class TestEmailValidator(unittest.TestCase):
    def test_valid_email(self):
        self.assertTrue(is_valid_email("test@example.com"))
        self.assertTrue(is_valid_email("test@example.org")) 
        self.assertFalse(is_valid_email("invalid-email@"))
        self.assertFalse(is_valid_email(""))

if __name__ == '__main__':
    unittest.main()
