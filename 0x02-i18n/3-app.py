#!/usr/bin/env python3
"""
    First you will setup a basic Flask app in 0-app.py.
    Create a single / route and an index.html template
    that simply outputs “Welcome to Holberton” as page
    title (<title>) and “Hello world” as header (<h1>).
"""
from flask import Flask, request
from flask import render_template
from flask_babel import Babel, gettext as _


class Config:
    """change default config in flask babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# create app instance and map the app to Babel
app = Flask(__name__)
app.config.from_object(Config)

# map app to Babel
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
        to determine the best match with our supported languages.
    """
    return request.accept_languages.best_match(app.Config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """
        the / root page
        renders basic html
    """
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
