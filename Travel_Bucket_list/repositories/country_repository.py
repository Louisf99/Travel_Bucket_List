from db.run_sql import run_sql
from models.country import Country
from models.city import City

#  Adding in CRUD functionality

# CREATE
def save(country):
    sql = "INSERT INTO countries (name, population, currency, language ) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [country.name, country.population, country.currency, country.language]
    results = run_sql(sql, values)
    id = results[0]['id']
    country.id = id
    return country

# READ Individual
def select(id):
    country = None
    sql = "SELECT * FROM countries WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        country = Country(result['name'], result['population'], result['currency'], result['language'], result['id'])
    return country
    
# READ all
def select_all():
    countries = []

    sql = "SELECT * FROM countries"
    results = run_sql(sql)

    for row in results:
        country = Country(row['name'], row['population'], row['currency'], row['language'], row['id'])
        countries.append(country)
    return countries

# UPDATE
def update(country):
    sql = "UPDATE countries SET (name, population, currency, language) = (%s, %s, %s, %s) WHERE id = %s"
    values = [country.name, country.population, country.currency, country.language]
    run_sql(sql, values)

# DELETE individual

# DELETE All


# List of all citites that match country_id
def cities(country):
    cities = []

    sql = "SELECT * FROM cities WHERE country_id = %s"
    values = [country.id]
    results = run_sql(sql, values)

    for row in results:
        city = City(row['name'], row['country_id'], row['visited'], row['id'] )
        cities.append(city)
    return cities