import factory
from factory.alchemy import SQLAlchemyModelFactory
from brprev_bot.database import db
from brprev_bot.models import Foo


class FooFactory(SQLAlchemyModelFactory):
    class Meta:
        model = Foo
        sqlalchemy_session = db.session

    description = factory.Sequence(lambda n: 'foo {0}'.format(n))
