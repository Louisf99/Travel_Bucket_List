from db.run_sql import run_sql
from models.country import Country
from models.city import City

def save(country):
    sql = "INSERT INTO countries (name) VALUES (%s) RETURNING *"
    values = [country.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    country.id = id
    return country

def update(country):
    sql = "UPDATE countries SET (name) = (%s) WHERE id = %s"
    values = [country.name, country.id]
    run_sql(sql, values)