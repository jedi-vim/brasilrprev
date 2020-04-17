import click

from brprev_bot.app import create_app
from brprev_bot.database import db


@click.command(name='initialize_db')
def initialize_db():
    app = create_app()
    with app.app_context():
        db.drop_all()
        db.create_all()


if __name__ == '__main__':
    initialize_db()
