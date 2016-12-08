from peewee import *
import datetime

db = SqliteDatabase('sample.db')


class Order(Model):
    id = PrimaryKeyField()
    date = DateTimeField(default=datetime.datetime.now)
    filial = CharField()
    text = TextField()

    class Meta:
        database = db


def initialize_db():
    db.connect()
    db.create_tables([Order], safe=True)
