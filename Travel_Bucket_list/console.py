import pdb
from models.city import City
from models.country import Country

import repositories.city_repository as city_repository
import repositories.country_repository as country_repository


country1 = Country("England", 58000000, "GBP", "English")
country_repository.save(country1)

country2 = Country("Scotland", 5800000, "GBP", "English")
country_repository.save(country2)

country3 = Country("Spain", 47000000, "Euro", "Spanish")
country_repository.save(country3)

country4 = Country("France", 67000000, "Euro", "France")
country_repository.save(country4)


# Test City repo fucntionality

city1 = City()







pdb.set_trace()
