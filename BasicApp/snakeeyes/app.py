from flask import Flask
from sqlalchemy.sql.elements import _defer_name

from snakeeyes.blueprints.page import page
from snakeeyes.extensions import db


def create_app(settings_override=None):
    """
    Create a Flask application using the app factory pattern.

    :param settings_override: Override settings
    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:tiger@localhost:5432/PhoneTool'

    if settings_override:
        app.config.update(settings_override)

    app.logger.setLevel(app.config['LOG_LEVEL'])
    app.register_blueprint(page)
    extensions(app)

    return app


def extensions(app):
    """
    Register 0 or more extensions (mutates the app passed in).

    :param app: Flask application instance
    :return: None
    """
    db.init_app(app)

    return None

if __name__ == '__main__':
    app = create_app()
    app.run()



