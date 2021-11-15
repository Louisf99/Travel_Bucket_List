from flask import Flask, render_template, request, redirect
from models.country import Country
from flask import Blueprint
from repositories import country_repository, user_repository
tasks_blueprint = Blueprint("countries", __name__)