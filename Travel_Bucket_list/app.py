from flask import Flask, blueprints, render_template
from controllers.travel_bucket_list import tasks_blueprint
from repositories import country_repository
app = Flask(__name__)
app.register_blueprint(tasks_blueprint)


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)