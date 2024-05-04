from datetime import datetime
from project import db
from enum import IntEnum
from sqlalchemy.dialects.mysql import TEXT


class BaseModel(db.Model):
    """基类模型
    """
    __abstract__ = True

    add_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, )  # 创建时间
    pub_date = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)  # 更新时间


class User(BaseModel):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), unique=True, nullable=False)
    email = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(320), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'