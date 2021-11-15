import unittest
from models.user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User("Ben Cooney", 22, "Scotland")

    def test_user_has_name(self):
        self.assertEqual("Ben Cooney", self.user.name)
    
    def test_user_has_age(self):
        self.assertEqual(22, self.user.age)
    
    def test_user_has_fav_country(self):
        self.assertEqual("Scotland", self.user.favourite_country)


    