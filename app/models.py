# from datetime import datetime
#
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import ForeignKey, Integer, Column
#
# db = SQLAlchemy()
#
#
#
#
# class Product(db.Model):
#     __tablename__='products'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)
#     image = db.Column(db.String)
#     section = db.Column(db.String)
#     description = db.Column(db.Text)
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)
#     updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)
#
#     def __str__(self):
#         return f"{self.name}"
#
#     @classmethod
#     def get_all_objects(cls):
#         return cls.query.all()
#
#
# class Section(db.Model):
#     __tablename__='section'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)
#     created_at = db.Column(db.DateTime, server_default=db.func.now())
#     updated_at = db.Column(db.DateTime,server_onupdate=db.func.now(), server_default=db.func.now())
#     product_id = db.Column(db.Integer, db.ForeignKey('products.id'))


from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, Integer, Column

db = SQLAlchemy()

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    image = db.Column(db.String)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)
    section_id = db.Column(db.Integer, db.ForeignKey('section.id'))
    section = db.relationship('Section', backref='products')

    def __str__(self):
        return f"{self.name}"

    @classmethod
    def get_all_objects(cls):
        return cls.query.all()


class Section(db.Model):
    __tablename__ = 'section'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_onupdate=db.func.now(), server_default=db.func.now())