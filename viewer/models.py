from django.db.models import CharField, Model, DateField, DateTimeField, FloatField, ForeignKey, TextField, DO_NOTHING,\
    IntegerField


class Genre(Model):
    name = CharField(max_length=128)


class Actor(Model):
    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)
    phone = CharField(max_length=20)
    email = CharField(max_length=20)
    salary = FloatField(default=10000.0)


class Movie(Model):
    title = CharField(max_length=128)
    genre = ForeignKey(Genre, on_delete=DO_NOTHING)
    rating = IntegerField(default=0)
    released = DateField()
    description = TextField()
    created = DateTimeField(auto_now_add=True)
