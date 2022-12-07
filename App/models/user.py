from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    authorId = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
   

    def __init__(self, username, password, authorId):
        self.username = username
        self.set_password(password)
        self.authorId = authorId

    def toJSON(self):
        return{
            'id': self.id,
            'username': self.username,
            'authorId': self.authorId
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

