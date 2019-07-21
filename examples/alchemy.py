# To be able to use this ORM you have to create postgresql database
# with exact credentials as below, and create table with name language and
# fields id, name.
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db_user = "postgres"
db_password = "coderslab"
db_host = "localhost"
db_name = "rest_api_flask"
app.config["SQLALCHEMY_DATABASE_URI"] = f'postgresql://{db_user}:{db_password}@{db_host}/{db_name}'
# instantiate DB objet
db = SQLAlchemy(app)


class Language(db.Model):
    # pass the name of existing table name in database
    __tablename__ = "language"

    # map the fields from table to class atributes.
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column("name", db.Unicode)
