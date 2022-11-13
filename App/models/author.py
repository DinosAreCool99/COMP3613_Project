from App.database import db
from datetime import *
from .author_publication import *

class Author(db.Model):
    __tablename__ = "author"
    id = db.Column(db.Integer, primary_key=True)
    name =  db.Column(db.String, nullable=False)
    dob = db.Column(db.DateTime, nullable=True)
    qualifications = db.Column(db.String(120), nullable=True)
    userId = db.Column(db.Integer, db.ForeignKey("user.id"), nullable = True)
    user = db.relationship('User', backref='user', uselist=False)
    publications = db.relationship("Publication", backref='user')

    def __init__(self, name, dob, qualifications):
        self.name = name
        if dob:
            self.dob = datetime.strptime(dob, "%d/%m/%Y")
        if qualifications:
            self.qualifications = qualifications

    def get_publications(self):
        return [publication.toJSON() for publication in self.publications]

    def toJSON(self):
        return{
            'id': self.id,
            'name': self.name,
            'dob': self.dob,
            'qualifications': self.qualifications,
            'userId': self.userId
        }

