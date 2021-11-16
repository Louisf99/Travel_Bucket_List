from db.run_sql import run_sql
from models.city import City
from models.country import Country
import repositories.country_repository as country_repository
# Adding in CRUD functionality

# CREATE
def save(city):
    sql = "INSERT INTO cities (name, country_id, visited) VALUES (%s, %s, %s) RETURNING *"
    values = [city.name, city.country.id, city.visited]
    results = run_sql(sql, values)
    id = results[0]['id']
    city.id = id
    return city

# READ individual
def select(id):
    city = None
    sql = "SELECT * FROM cities WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        country = country_repository.select(result['country_id'])
        city = City(result['name'], country, result['visited'], result['id'] )
    return city
# READ All
def select_all():
    cities = []

    sql = "SELECT * FROM cities"
    results = run_sql(sql)

    for row in results:
        country = country_repository.select(row['country_id'])
        city = City(row['name'], country, row['visited'], row['id'] )
        cities.append(city)
    return cities

# UPDATE
def update(city):
    sql = "UPDATE cities SET (name, country_id, visited) = (%s, %s, %s) WHERE id = %s"
    values = [city.name, city.country.id, city.visited, city.id]
    run_sql(sql, values)

# DELETE individual
def delete(id):
    sql = "DELETE  FROM cities WHERE id = %s"
    values = [id]
    run_sql(sql, values)
    
# DELETE  ALL
def delete_all():
    sql = "DELETE  FROM cities"
    run_sql(sql)



# READ function to gather data for all citites visoted and those that hav e not been visted, aka gather all values set to False for Not visted and all True for visited 

# NOT Visited
def select_all_not_visited():
    not_visited = []

    sql = "SELECT * FROM cities WHERE visited = %s"
    values = [False]
    results = run_sql(sql, values)

    for row in results:
        country = country_repository.select(row['country_id'])
        city = City(row['name'], country, row['visited'], row['id'] )
        not_visited.append(city)
    return not_visited

# Visited 
def select_all_visited():
    cities_visited = []

    sql = "SELECT * FROM cities WHERE visited = %s"
    values = [True]
    results = run_sql(sql, values)

    for row in results:
        country = country_repository.select(row['country_id'])
        city = City(row['name'], country, row['visited'], row['id'] )
        cities_visited.append(city)
    return cities_visited
