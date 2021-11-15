import unittest
from models.user import User

class TestCountry(unittest.TestCase):
    def setUp(self):
        self.user = User("Ben Cooney", 22, "Scotland")

    def test_user_has_name(self):
        self.assertEqual("Ben Cooney", self.customer.name)

    