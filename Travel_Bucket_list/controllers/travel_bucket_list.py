from flask import Flask, render_template, redirect, request
from flask import Blueprint
from models.city import City
from models.country import Country
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

cities_blueprint = Blueprint("cities", __name__)


@cities_blueprint.route('/cities', methods=['GET'])
def destinations():
    cities = city_repository.select_all()
    print(cities)
    return render_template('cities/index.html', cities=cities)

@cities_blueprint.route('/cities/visited', methods=['GET'])
def visited_cities():
    all_visited_cities = city_repository.select_all_visited()
    return render_template('/cities/visited.html', all_visited_cities = all_visited_cities)

@cities_blueprint.route('/cities/not_visited', methods=['GET'])
def not_visited_cities():
    not_visited_cities = city_repository.select_all_not_visited()
    return render_template("/cities/not_visited.html", not_visited_cities = not_visited_cities)

@cities_blueprint.route('/cities/<id>/delete', methods=['POST'])
def delete_city(id):
    city_repository.delete(id)
    return redirect('/cities')

@cities_blueprint.route('/cities/new_destination', methods=['GET'])
def new_city():
    countries = country_repository.select_all()
    return render_template('cities/add_city.html', all_countries=countries)

@cities_blueprint.route('/cities', methods=['POST'])
def create_city():
    name = request.form['name']
    country_id = request.form['country_id']
    visited = request.form['visited']
    country = country_repository.select(country_id)
    city = City(name, country, visited)
    city_repository.save(city)
    return redirect('/cities')