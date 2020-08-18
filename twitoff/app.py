"""Main app/routing file for TwitOff."""
from flask import Flask, render_template


def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)

    @app.route('/')
    def root():
        return render_template('base.html', title='Home')
    return app