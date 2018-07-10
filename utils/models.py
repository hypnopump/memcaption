from __init__ import app, db


class Img(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(150))
    user = db.Column(db.String(50))
    source = db.Column(db.String(100))
    source_link = db.Column(db.Text)

    def __init__(self, name, user, source, source_link):
        self.name = name
        self.user = user
        self.source = source
        self.source_link = source_link

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.Text)
    username = db.Column(db.String(50))
    score = db.Column(db.Integer)
    img_id = db.Column(db.Integer)
    img_name = db.Column(db.String(150))

    def __init__(self, text, username, score, img_id, img_name):
        self.text = text
        self.username = username
        self.score = score
        self.img_id = img_id
        self.img_name = img_name
