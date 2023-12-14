from datetime import datetime
from project import db
from enum import IntEnum
from sqlalchemy.dialects.mysql import TEXT


# class BaseModel(db.Model):
#     """基类模型
#     """
#     __abstract__ = True
#
#     add_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, ) # 创建时间
#     pub_date = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False) # 更新时间

class Category(db.Model):
    """分类模型
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    # icon = db.Column(db.String(128), nullable=True)
    # add_date = db.Column(db.Datetime, nullable=False, default=datetime.utcnow())
    # pub_date = db.Column(db.Datetime, nullable=False, default=datetime.utcnow(), onupdate=datetime.utcnow())
    # news = db.relationship('News', backref='category', lazy=True)

    def __repr__(self):
        return f'<Category {self.name}>'


class News(db.Model):
    """新闻模型
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    content = db.Column(TEXT, nullable=False)
    # category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    office = db.Column(db.String(128), nullable=True)
    source = db.Column(db.String(128), nullable=True)
    time = db.Column(db.String(128), nullable=False)
    location = db.Column(db.String(128), nullable=True)
    link = db.Column(db.String(128), nullable=False)
    comments_count = db.Column(db.Integer, nullable=True)
    participants = db.Column(db.Integer, nullable=True)
    keywords = db.Column(db.String(128), nullable=True)
    picture = db.Column(db.String(128), nullable=True)
    category = db.Column(db.String(128), nullable=False)
    comment1 = db.Column(TEXT, nullable=True)
    comment2 = db.Column(TEXT, nullable=True)
    comment3 = db.Column(TEXT, nullable=True)
    comment4 = db.Column(TEXT, nullable=True)
    comment5 = db.Column(TEXT, nullable=True)
    comment6 = db.Column(TEXT, nullable=True)
    comment7 = db.Column(TEXT, nullable=True)
    comment8 = db.Column(TEXT, nullable=True)
    comment9 = db.Column(TEXT, nullable=True)
    comment10 = db.Column(TEXT, nullable=True)

    def __repr__(self):
        return f'<Post {self.title}>'
