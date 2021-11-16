from flask import Flask, render_template, redirect, request
from flask import Blueprint

from models.city import City
from models.country import Country

import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

country_blueprint = Blueprint("country", __name__)