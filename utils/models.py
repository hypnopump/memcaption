from __init__ import app, db

class Reg(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(150))
    hash = db.Column(db.String(75))

    def __init__(self, name, hash):
        self.name = name
        self.hash = hash