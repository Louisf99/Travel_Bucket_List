import unittest
from models.user import User

class TestCountry(unittest.TestCase):
    def setUp(self):
        self.user = User()