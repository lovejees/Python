from flask import Flask
from snakeeyes.tests.extensions import debug_toolbar

from snakeeyes.blueprints.page import page

"""
Create a Flask application using the app factory pattern.

:return: Flask app
"""
app = Flask(__name__, instance_relative_config=True)

app.config.from_object('config.settings')
app.config.from_pyfile('settings.py', silent=True)

app.register_blueprint(page)
# extension(app)


def extension(app):
    debug_toolbar.init_app(app)
