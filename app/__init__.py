from flask import Flask
from .api.routes import api
from .extensions import db
from flask.cli import with_appcontext
import click
import load_data.weather
import load_data.yield_data
from flask_migrate import Migrate
def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    migrate = Migrate(app,db)

    app.register_blueprint(api)
    db.init_app(app)

    # custom command to upload weather data
    @click.command(name='upload')
    @with_appcontext
    def upload():
        load_data.weather.main()

    # custom command to upload yield data
    @click.command(name='upload_yield')
    @with_appcontext
    def upload_yield():
        load_data.yield_data.main()

    app.cli.add_command(upload)
    app.cli.add_command(upload_yield)

    return app