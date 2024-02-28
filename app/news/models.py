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


    def __repr__(self):
        return f'<Category {self.name}>'


class News(db.Model):
    """新闻模型
    """
    id = db.Column(db.Integer, primary_key=True)
    rate = db.Column(db.String(16), nullable=False)
    authority = db.Column(db.String(64), nullable=True)
    source = db.Column(db.String(64), nullable=False)
    source_url = db.Column(db.String(128), nullable=False)
    date = db.Column(db.String(32), nullable=False)
    title = db.Column(db.String(128), nullable=False)
    content = db.Column(TEXT, nullable=False)
    forward_num = db.Column(db.Integer, nullable=False)
    comment_num = db.Column(db.Integer, nullable=False)
    like_num = db.Column(db.Integer, nullable=False)
    detail_url = db.Column(db.String(128), nullable=False)
    # category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)

    def __repr__(self):
        return f'<Post {self.title}>'
