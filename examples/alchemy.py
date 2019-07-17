from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config("SQLALCHEMY_DATABASE_URI") = 'postgresql://postgres:coderslab@localhost/rest_api_flask'
# instantiate DB objet
db = SQLAlchemy(app)


class Language(db.Model):
    __tablename__ = "language"

    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column("name", db.Unicode)
