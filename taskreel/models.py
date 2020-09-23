from flask_login import UserMixin
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from . import db

app = Flask(__name__)

app.config['SQLALchemy_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/studyapp'

db = SQLAlchemy(app)

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    reelemxs = db.relationship('Reelemx', backref = 'user', lazy = True)


class Reelemx(db.Model):
    __tablename__ = 'reelemxs'

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String, nullable=False)
    title = db.Column(db.String(150))
    # this set a one to many relationship between USERS and Reelemx
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='SET NULL'))
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    

    def __repr__(self):
        return f"Reelemx(id={self.id}, title={self.title}, user_id={self.user_id})"

# class Prtapl(db.Model):
#     __tablename__ = 'prtapls'

#     id = db.Column(db.Integer, primary_key=True)
#     Prtapl = db.Column(db.String(50), unique=True, nullable=False)
#     reelemx_id = db.Column(db.Integer, db.ForeignKey('reelemxs.id', ondelete='SET NULL'))
#     def __repr__(self):
#         return f"Prtapl(id={self.id}, prtapl={self.prtapl})"
#     def as_dict(self):
#         return {c.name: getattr(self, c.name) for c in self.__table__.columns}