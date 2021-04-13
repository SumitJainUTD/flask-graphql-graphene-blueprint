from flask import Flask
from .extenstions import db
from .routes.blueprint_company import company
from .routes.blueprint_home import home


def create_app(config_file='settings.py'):
    app = Flask(__name__)

    app.config.from_pyfile(config_file)
    db.init_app(app)
    app.register_blueprint(company, url_prefix="/company")
    app.register_blueprint(home)
    return app

