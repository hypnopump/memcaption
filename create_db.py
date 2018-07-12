from __init__ import db
from utils.models import User, Comment, Img

db.create_all()

db.session.add(User("Eric Alcaide", " ericalcaide1@gmail.com", "18933db28dbe16a2e6c99c4d7ea53d370c4d214b604c5301f27714a114f7c7e9"))
# db.session.add(User("George Orwell", "kytorch@gmail.com", "0a0d1178725d8c146133786adce09b3f2a6c6414e76ab31b26d28af8a1e22f5c"))

db.session.add(Comment("Eric Alcaide", "'Tomorrow is Monday'", 1, 0, ""))
# db.session.add(Comment("George Orwell", "when you expect A+ but get C", 1, 0, ""))

db.session.add(Img("first.png", "Pexels", "pexels.com"))
db.session.add(Img("second.png", "Pexels", "pexels.com"))

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
