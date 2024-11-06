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
from typing import Union


class Config:
    """
        change default config in flask babel
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# create app instance and map the app to Babel
app = Flask(__name__)
app.config.from_object(Config)

# map app to Babel
babel = Babel(app)


@babel.localeselector
def get_locale() -> Union[str, None]:
    """
        to determine the best match with our supported languages.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """
        the / root page
        renders basic html
    """
    locale = get_locale()
    return render_template('3-index.html', locale=locale)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
