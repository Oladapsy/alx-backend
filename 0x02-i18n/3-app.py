#!/usr/bin/env python3
"""
    First you will setup a basic Flask app in 0-app.py.
    Create a single / route and an index.html template
    that simply outputs “Welcome to Holberton” as page
    title (<title>) and “Hello world” as header (<h1>).
"""
from flask import Flask, request, render_template
from flask import render_template
from flask_babel import Babel


class Config(object):
    """change default config in flask babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
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
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
