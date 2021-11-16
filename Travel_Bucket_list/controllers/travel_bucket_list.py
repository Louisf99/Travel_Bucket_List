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
    return render_template("cities/index.html", cities=cities)

@cities_blueprint.route("/cities/visited", methods=['GET'])
def visited_cities():
    all_visited_cities = city_repository.select_all_visited()
    return render_template("/cities/visited.html", all_visited_cities = all_visited_cities)
