import pdb
from models.city import City
from models.country import Country

import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

# Testing CRUD functionality for country repo

# Test CREATE
country1 = Country("England", 58000000, "GBP", "English")
country_repository.save(country1)

country2 = Country("Scotland", 5800000, "GBP", "English")
country_repository.save(country2)

country3 = Country("Spain", 47000000, "Euro", "Spanish")
country_repository.save(country3)

country4 = Country("France", 67000000, "Euro", "French")
country_repository.save(country4)

# Test READ

# Test UPDATE

# Test DELETE



# Test City repo fucntionality

# Test CREATE
city1 = City("London", country1)
city_repository.save(city1)

city2 = City("Edinburgh", country2, True)
city_repository.save(city2)

city3 = City("Madrid", country3)
city_repository.save(city3)

city4 = City("Paris", country4, True)
city_repository.save(city4)

# Test READ

# Test UPDATE

# Test DELETE
# city_repository.delete(1)



pdb.set_trace()
