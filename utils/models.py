from __init__ import app, db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(150))
    email = db.Column(db.String(150))
    password = db.Column(db.String(150))

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password