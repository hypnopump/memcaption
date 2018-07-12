from __init__ import db
from utils.models import User, Comment, Img

db.create_all()

db.session.add(User("Eric Alcaide", " ericalcaide1@gmail.com", "18933DB28DBE16A2E6C99C4D7EA53D370C4D214B604C5301F27714A114F7C7E9"))
db.session.add(User("Geroge Orwell", "kytorch@gmail.com", "0A0D1178725D8C146133786ADCE09B3F2A6C6414E76AB31B26D28AF8A1E22F5C"))

db.session.add(Comment("eric_alcaide", "me in the mornin'", 1, 0))
db.session.add(Comment("George Orwell", "when you expect A+ but get C", 1, 0))

db.session.add(Comment("first.png", "Pexels", "pexels.com", 0))
db.session.add(Comment("second.png", "Pexels", "pexels.com", 0))

db.session.commit()

# UNIT TESTING TO GUARANTEE DB CREATION 
# PUSH TO HEROKU
# heroku run python create_db.py 

# heroku run python
# from __init__ import db
# from utils.models import XXXX
# q = XXXX.query.all()
# lister = [[line.] for line in q]
# print(lister)
