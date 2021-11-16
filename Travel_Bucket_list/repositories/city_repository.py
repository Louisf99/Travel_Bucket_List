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

# READ 

# UPDATE

# DELETE individual
def delete(id):
    sql = "DELETE  FROM cities WHERE id = %s"
    values = [id]
    run_sql(sql, values)
    
# DELETE  ALL