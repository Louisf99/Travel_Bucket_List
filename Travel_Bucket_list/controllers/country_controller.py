from flask import Flask, render_template, redirect, request
from flask import Blueprint

from models.city import City
from models.country import Country

import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

country_blueprint = Blueprint("country", __name__)

@country_blueprint.route("/country")
def country():
    countries = country_repository.select_all()
    print(countries)
    return render_template("countries/index.html", countries = countries)


@country_blueprint.route("/country/new", methods = ['GET'])
def new_country():
    return render_template("/countries/add_country.html")


@country_blueprint.route("/country", methods = ['POST'])
def create_country():
    name = request.form['name']
    population = request.form['population']
    currency = request.form['currency']
    language = request.form['language']
    country = Country(name, population, currency, language)
    country_repository.save(country)
    return redirect('/country')

@country_blueprint.route('/country/<id>/delete', methods=['POST'])
def delete_country(id):
    country_repository.delete(id)
    return redirect('/country')



@country_blueprint.route('/country/<id>', methods=['GET'])
def show_country(id):
    country = country_repository.select(id)
    return render_template('countries/show.html', country=country)

# EDIT
@country_blueprint.route('/country/<id>/edit', methods=['GET'])
def edit_country(id):
    country = country_repository.select(id)
    return render_template('countries/edit_country.html',  country = country)


# UPDATE
@country_blueprint.route('/country/<id>/edit', methods=['POST'])
def update_country(id):
    name = request.form['name']
    population = request.form['population']
    currency = request.form['currency']
    language = request.form['language']
    country = Country(name, population, currency, language, id)
    country_repository.update(country)
    return redirect('/country')
