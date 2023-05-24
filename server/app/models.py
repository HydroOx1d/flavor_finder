from sqlalchemy import ForeignKey, CheckConstraint
from app import db

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True) 
    username = db.Column(db.String(80), unique=True, nullable=False) 
    email = db.Column(db.String(120), unique=True, nullable=False) 
    password = db.Column(db.String(60), nullable=False) 

class Place(db.Model):
    __tablename__ = 'places'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255))
    rating = db.Column(db.Integer)
    num_reviews = db.Column(db.Integer)
    average_price = db.Column(db.Numeric)
    map_link = db.Column(db.String(255))

    __table_args__ = (
        CheckConstraint(rating.between(1, 5), name='rating_range_check'),
    )

    def __repr__(self):
        return f"<Place(id={self.id}, name='{self.name}', address='{self.address}', rating={self.rating}, num_reviews={self.num_reviews}, average_price={self.average_price}, map_link='{self.map_link}')>"

class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_name = db.Column(db.String(255), nullable=False)
    review = db.Column(db.String(1000))
    rating = db.Column(db.Integer)
    address = db.Column(db.String(255))
    place_id = db.Column(db.Integer, ForeignKey('places.id'))

    __table_args__ = (
        CheckConstraint(rating.between(1, 5), name='rating_range_check'),
    )
    
    def __repr__(self):
        return f"<Comment(id={self.id}, user_name='{self.user_name}', review='{self.review}', rating={self.rating}, address='{self.address}', place_id={self.place_id})>"