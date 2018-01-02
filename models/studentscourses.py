import config
# from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from student import student
from course import course


db = config.db


class studentscourses(UserMixin, db.Model):

    __tablename__ = 'studentscourses'
    id = db.Column('id', db.Integer, primary_key = True)
    sid = db.Column(db.Integer,db.ForeignKey('student.id'),nullable=False )
    cid = db.Column(db.Integer,db.ForeignKey('course.id'),nullable=False )

    # student = db.relationship(
    #     student,
    #     backref=db.backref('studentscourses',
    #                      uselist=True,
    #                      cascade='delete,all'))
    #
    # course = db.relationship(
    #     course,
    #     backref=db.backref('studentscourses',
    #                      uselist=True,
    #                      cascade='delete,all'))

    def update(self):
        db.session.commit()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __init__(self, id, name, password):
        self.id= sid
        self.name = name.lower()
        self.password = password()


    def __repr__(self):
        return '<Student id %d is taking course id %d>' % (self.sid, self.cid)
