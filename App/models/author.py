from App.database import db
from datetime import *
from .author_publication import *

class Author(db.Model):
    __tablename__ = "author"
    id = db.Column(db.Integer, primary_key=True)
    name =  db.Column(db.String, nullable=False)
    dob = db.Column(db.DateTime, nullable=True)
    qualifications = db.Column(db.String(120), nullable=True)
    user = db.relationship('User', backref='user', uselist=False)
    publications = db.relationship("Publication", backref='user')

    def __init__(self, name, dob, qualifications):
        self.name = name
        if dob:
            self.dob = datetime.strptime(dob.strftime("%d/%m/%Y %H:%M:%S"), "%d/%m/%Y %H:%M:%S") #convert dob to string so it
        if qualifications:
            self.qualifications = qualifications

    def get_publications(self):
        return [publication.toJSON() for publication in self.publications]

    def set_user(self, user):
        self.user = user

    def toJSON(self):
        return{
            'id': self.id,
            'name': self.name,
            'dob': self.dob,
            'qualifications': self.qualifications,
        }

