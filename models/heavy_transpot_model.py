# coding: utf-8
import config
from sqlalchemy.orm import relationship

db = config.db

class Client(db.Model):
    __tablename__ = 'client'

    client_id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(50, u'utf8_bin'), nullable=False)
    client_type = db.Column(db.Integer, nullable=False)


class Invoice(db.Model):
    __tablename__ = 'invoice'

    invoice_id = db.Column(db.Integer, primary_key=True)
    provider_id = db.Column(db.ForeignKey(u'provider.provider_id'), nullable=False, index=True)
    client_id = db.Column(db.ForeignKey(u'client.client_id'), nullable=False, index=True)
    office_id = db.Column(db.ForeignKey(u'office.office_id'), nullable=False, index=True)

    client = db.relationship(u'Client', primaryjoin='Invoice.client_id == Client.client_id', backref=u'invoices')
    office = db.relationship(u'Office', primaryjoin='Invoice.office_id == Office.office_id', backref=u'invoices')
    provider = db.relationship(u'Provider', primaryjoin='Invoice.provider_id == Provider.provider_id', backref=u'invoices')


class Office(db.Model):
    __tablename__ = 'office'

    office_id = db.Column(db.Integer, primary_key=True)
    office_name = db.Column(db.String(50, u'utf8_bin'), nullable=False)


class Provider(db.Model):
    __tablename__ = 'provider'

    provider_id = db.Column(db.Integer, primary_key=True)
    provider_name = db.Column(db.String(50, u'utf8_bin'), nullable=False)
    provider_type = db.Column(db.Integer, nullable=False)
