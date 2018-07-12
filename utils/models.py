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
    voters = db.Column(db.Text)

    def __init__(self, username, text, img_id, score, voters):
        self.username = username
        self.text = text
        self.img_id = img_id
        self.score = score
        self.voters = voters

class Img(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(42))
    source_name = db.Column(db.String(42*2))
    source_link = db.Column(db.String(42*2))

    def __init__(self, name, source_name, source_link):
        self.name = name
        self.source_name = source_name
        self.source_link = source_link