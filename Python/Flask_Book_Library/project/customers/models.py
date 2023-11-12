from project import db, app
import re


# Customer model
class Customer(db.Model):
    __tablename__ = "customers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    city = db.Column(db.String(64))
    age = db.Column(db.Integer)

    def __init__(self, name, city, age):
        if not re.match("^[a-zA-Z]{1,12}$", name):
            raise ValueError("Name must contain only letters and the max length is 12.")
        if not re.match("^[a-zA-Z ]{1,20}$", city):
            raise ValueError("City must contain only letters and the max length is 20.")
        self.name = name
        self.city = city
        self.age = age

    def __repr__(self):
        return f"Customer(ID: {self.id}, Name: {self.name}, City: {self.city}, Age: {self.age})"


with app.app_context():
    db.create_all()
