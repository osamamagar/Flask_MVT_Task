from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()




class Product(db.Model):
    # __tablename__='students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    image = db.Column(db.String)
    section = db.Column(db.String)
    # dept_id = db.Column(db.Integer, db.ForeignKey('tracks.id'), nullable=True)


class Section(db.Model):
    # __tablename__='tracks'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime,server_onupdate=db.func.now(), server_default=db.func.now())
    product= db.relationship('Product', backref='track_name', lazy=True)
