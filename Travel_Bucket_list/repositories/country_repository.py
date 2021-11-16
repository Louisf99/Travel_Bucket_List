from db.run_sql import run_sql
from models.country import Country
from models.city import City

def save(country):
    sql = "INSERT INTO countries (name, population, currency, language ) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [country.name, country.population, country.currency, country.language]
    results = run_sql(sql, values)
    id = results[0]['id']
    country.id = id
    return country

def update(country):
    sql = "UPDATE countries SET (name, population, currency, language) = (%s, %s, %s, %s) WHERE id = %s"
    values = [country.name, country.population, country.currency, country.language]
    run_sql(sql, values)

def cities(country):
    cities = []

    sql = "SELECT * FROM cities WHERE country_id = %s"
    values = [country.id]
    results = run_sql(sql, values)

    for row in results:
        city = City(row['name'], row['country_id'], row['visited'], row['id'] )
        cities.append(city)
    return cities