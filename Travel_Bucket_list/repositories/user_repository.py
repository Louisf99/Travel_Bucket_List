from db.run_sql import run_sql

from models.user import User
from models.country import Country


def save(user):
    sql = "INSERT INTO users (name, age, favourite_country) VALUES (%s, %s, %s) RETURNING *"
    values = [user.name, user.age]
    results = run_sql(sql, values)
    id = results[0]['id']
    user.id = id
    return user

def countries(user):
    countries = []

    sql = "SELECT * FROM tasks WHERE user_id = %s"
    values = [user.id]
    results = run_sql(sql, values)

    for row in results:
        country = Country(row['name'], row['user_id'], row['population'], row['city'], row['currency'], row['langauge'], row['visited'],row['id'] )
        countries.append(country)
    return countries
