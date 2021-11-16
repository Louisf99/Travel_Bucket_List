from flask import Flask, render_template, redirect, request
from flask import Blueprint
from models.city import City
from models.country import Country
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

destination_blueprint = Blueprint("destinations", __name__)


@destination_blueprint.route('/destinations')
def destinations():
    destinations = city_repository.select_all()
    print(destinations)
    return render_template("destination/index.html", destinations=destinations)
    