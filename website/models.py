from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Plant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    seeding_time = db.Column(db.String(150))
    harvest_time = db.Column(db.String(150))
    heat_demand = db.Column(db.Float)
    nutrient_requierements = db.Column(db.String(150))
    light_requierement = db.Column(db.String(150))
    properties = db.Column(db.String(500))
    pic = db.Column(db.String(150))
    place_points = db.Column(db.Integer)

class User(db.model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True)
    name = db.Column(db.String(150), nullable=False)
    family_name = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(150), nullable=False)

class Seeding(db.model):
    id = db.Column(db.Integer, primary_key=True)
    plant_id = db.Column(db.Integer, db.ForeignKey('plant.id'), nullable=False)
    sowing_date = db.Column(db.DateTime)
    plant_date = db.Column(db.DateTime)
    qty = db.Column(db.Integer)
    place_points = db.Column(db.Integer)
    

class 

    


"""
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')
"""
