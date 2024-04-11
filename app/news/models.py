from datetime import datetime
from project import db
from enum import IntEnum
from sqlalchemy.dialects.mysql import TEXT


class BaseModel(db.Model):
    """基类模型
    """
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    rate = db.Column(db.Integer, nullable=False)
    authority = db.Column(db.String(64), nullable=True)
    source = db.Column(db.String(64), nullable=False)
    source_url = db.Column(db.String(128), nullable=False)
    date = db.Column(db.Date, nullable=False)
    title = db.Column(db.String(128), nullable=False)
    content = db.Column(TEXT, nullable=False)
    forward_num = db.Column(db.Integer, nullable=False)
    comment_num = db.Column(db.Integer, nullable=False)
    like_num = db.Column(db.Integer, nullable=False)
    detail_url = db.Column(db.String(128), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)

class Category(db.Model):
    """分类模型
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    news = db.relationship('News', backref='category', lazy=True)
    refute = db.relationship('Refute', backref='category', lazy=True)
    rumors = db.relationship('Rumors', backref='category', lazy=True)
    def __repr__(self):
        return f'<Category {self.name}>'


class News(BaseModel):
    """新闻模型
    """

    def __repr__(self):
        return f'<Post {self.title}>'

class Refute(BaseModel):
    """辟谣模型
    """

    def __repr__(self):
        return f'<Refute {self.title}>'

class Rumors(BaseModel):
    """辟谣模型
    """

    def __repr__(self):
        return f'<Rumors {self.title}>'

class Follows(BaseModel):
    """溯谣模型
    """
    follow_link = db.Column(db.String(1024), nullable=False)
    follow_content = db.Column(TEXT, nullable=False)
    def __repr__(self):
        return f'<Rumors {self.title}>'