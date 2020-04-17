from dynaconf import FlaskDynaconf, settings
from flask import Flask

from brprev_bot import views
from brprev_bot.database import db


def create_app():
    app = Flask(__name__)

    FlaskDynaconf(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = settings.get('PG_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    views.init_app(app)
    return app
