import config
# from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from instructor import instructor


db = config.db


class course(UserMixin, db.Model):

    __tablename__ = 'courses'
    id = db.Column('id', db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable=False)
    start_time = db.Column(db.Time,nullable=False)
    end_time = db.Column(db.Time,nullable=False)
    iid = db.Column(db.Integer,db.ForeignKey('instructor.iid'),nullable=False )
    days = db.Column(db.Unicode(5), nullable=False)
    location = db.Column(db.Unicode(250), nullable=False)
    # instructor = db.relationship(
    #     instructor,
    #     backref=db.backref('course',
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
        return '<the course is %r>' % self.name
