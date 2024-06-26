import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from project.settings import BASE_DIR
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def inject_news():
    # 上下文处理器回调函数
    """
    context_processor上下文处理器在呈现模板之前运行，并且能够将新值注入模板上下文。上下文处理器是返回字典的函数。
    然后，对于应用程序中的所有模板，此字典的键和值将与模板上下文合并：
    """
    from app.news.models import News
    # categorys = News.query.limit(6).all()
    news = News.query.all()
    return dict(news=news)


def register_bp(app:Flask):
    # 注册视图方法
    from app.news import views as news
    # 注册蓝图
    app.register_blueprint(news.bp)
    from app.user import views as user
    app.register_blueprint(user.bp)
    # 首页url 这个的意思是定义整个网站的首页url是 '/', 这个首页来源于news.index, news.index的url是'/news/index'
    app.add_url_rule(rule='/', endpoint='index', view_func=news.index)


def create_app(test_config=None):
    # 创建Flask对象 最重要！！！
    app = Flask(__name__, instance_relative_config=True)

    # 这里做了判断是否运行时传入了测试配置
    if test_config is None:
        # 如果没有传入，则从py文件加载配置，silent=True代表文件，文件加载成功则返回True
        CONFIG_PATH = BASE_DIR / 'project/settings.py'
        app.config.from_pyfile(CONFIG_PATH, silent=True)
    else:
        # 和最开始的配置意思一致
        app.config.from_mapping(test_config)

    # 递归创建目录，确保项目文件存在
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # 绑定数据库
    db.init_app(app)

    # 注册migrate
    migrate.init_app(app, db)

    # 从此处开始注册蓝图
    register_bp(app)

    # 注册模型
    from app.news import models

    # 全局上下文
    app.context_processor(inject_news)

    return app

