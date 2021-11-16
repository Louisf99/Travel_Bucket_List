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

country4 = Country("France", 67000000, "Euro", "French")
country_repository.save(country4)

country3.language = "French"
country_repository.update(country3)


# Test City repo fucntionality

city1 = City("London", country1)
city_repository.save(city1)

city2 = City("Edinburgh", country2, True)
city_repository.save(city2)

city_repository.delete(1)

pdb.set_trace()
