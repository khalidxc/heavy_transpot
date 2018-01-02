import config
# from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

db = config.db


class instructor(UserMixin, db.Model):

    __tablename__ = 'instructor'
    iid = db.Column('iid', db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable=False)
    mail = db.Column(db.String(30), nullable=False)
    Ipassword = db.Column(db.Unicode(20), nullable=False)

    def update(self):
        db.session.commit()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __init__(self, username, mail, password):
        self.username = username.lower()
        self.name = username
        self.mail = mail.lower()
        self.Ipassword = mail.lower()
    # def listSections(self):
    #     return sections= db.query.all()




    def __repr__(self):
        return '<instructor is %r>' % self.name
