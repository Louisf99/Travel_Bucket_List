import unittest
from models.country import Country

class TestCountry(unittest.TestCase):
    def setUp(self):
        self.country = Country("England", 58000000, "London", "GBP", "English", True)

    def test_country_has_name(self):
        self.assertEqual("England", self.country.name)
    
    def test_country_has_population(self):
        self.assertEqual(58000000, self.country.population)

    def test_country_has_city(self):
        self.assertEqual("London", self.country.city)

    def test_country_has_currency(self):
        self.assertEqual("GBP", self.country.currency)

    def test_country_has_language(self):
        self.assertEqual("English", self.country.language)

    def test_country_visit(self):
        self.assertEqual(True, self.country.visited)

        
