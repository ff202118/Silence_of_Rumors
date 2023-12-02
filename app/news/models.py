from datetime import datetime
from project import db
from enum import IntEnum
from sqlalchemy.dialects.mysql import LONGTEXT

class BaseModel(db.Model):
    """基类模型
    """
    __abstract__ = True

    add_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, ) # 创建时间
    pub_date = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False) # 更新时间

class Category(db.Model):
    """分类模型
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    icon = db.Column(db.String(128), nullable=True)
    add_date = db.Column(db.Datetime, nullable=False, default=datetime.utcnow())
    pub_date = db.Column(db.Datetime, nullable=False, default=datetime.utcnow(), onupdate=datetime.utcnow())

    def __repr__(self):
        return '<Category %r>>' % self.name