import config
# from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

db = config.db


class student(UserMixin, db.Model):

    __tablename__ = 'student'
    id = db.Column('id', db.Integer, primary_key = True)
    sid = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    password = db.Column(db.Unicode(20), nullable=False)

    def update(self):
        db.session.commit()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __init__(self, sid, name, password):
        self.sid= sid
        self.name = name.lower()
        self.password = password()


    def __repr__(self):
        return '<student is %r>' % self.name
