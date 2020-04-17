from functools import wraps
from brprev_bot.app import create_app


def flask_context(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        app = create_app()
        with app.app_context():
            fn(*args, **kwargs)
    return wrapper
