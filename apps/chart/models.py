from datetime import date
from multiprocessing.sharedctypes import Value
from flask_login import UserMixin

from apps import db, login_manager

class Dates(db.Model):
    __tablename__ = 'Dates'
    id = db.Column(db.Integer, primary_key = True)
    dates = db.Column(db.String(100))

class Value(db.Model):
    __tablename__ = 'Values'
    id = db.Column(db.Integer, primary_key = True)
    values = db.Column(db.String(100))
    fk_date_id = db.Column(db.Integer)