from flask import Flask, blueprints, render_template
from controllers.travel_bucket_list import destination_blueprint
from repositories import city_repository, country_repository
app = Flask(__name__)
app.register_blueprint(destination_blueprint)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True)