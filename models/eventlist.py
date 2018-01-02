import config
# from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
import json
db = config.db


class eventlist(UserMixin, db.Model):

    __tablename__ = 'eventlist'
    id = db.Column('id', db.Integer, primary_key = True)
    weight = db.Column(db.Integer, nullable=True)
    name = db.Column(db.String(50), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    description = db.Column(db.Text, nullable=True)


    def update(self):
        db.session.commit()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __init__(self, sid, name, password):
        self.id= sid
        self.name = name.lower()
        self.description = description

    def jsonEvents(self):
        colorCode= 255- self.weight*25
        color= 'rgb(255,%d,%d)' % (colorCode,colorCode)
        # print type(self.start_date
        dateOfEvent=self.start_date.strftime("%Y-%m-%d")
        # startingDate= '-'.join(str(x) for x in (self.start_date.year, self.start_date.month, self.start_date.day))

        sd=''+dateOfEvent
        d= {'title': self.name, 'start': sd,'color':color}
        return d

    def __repr__(self):
        # d= {'title': self.name, 'start': '2015-02-01'}
        # return json.dumps(d)
        return '{"title":  %r , "start": "2015-02-01"}' % self.name
