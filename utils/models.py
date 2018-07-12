from __init__ import app, db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(42))
    email = db.Column(db.String(150))
    password = db.Column(db.String(150))

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(42))
    text = db.Column(db.Text)
    img_id = db.Column(db.Integer)
    score = db.Column(db.Integer)

    def __init__(self, username, text, img_id, score):
        self.username = username
        self.text = text
        self.img_id = img_id
        self.score = score