from flask import Blueprint, render_template, request
from .models import News
from datetime import datetime
from sqlalchemy import func, cast, Date
from project import db
import pickle as pkl

# 注意此处蓝图的注册
bp = Blueprint('news', __name__, url_prefix='/news', static_folder='static', template_folder='templates')

# http://127.0.0.1:5000/news/index/

@bp.route('index/')
def index():
    page = request.args.get('page', 1, type=int)
    pagination = News.query.paginate(page=page, per_page=10, error_out=False)

    post_list = pagination.items

    for post in post_list:
        post.authority = post.authority.replace('@', '')
        post.date = post.date.replace('.000', '')

    return render_template('index.html', posts=post_list, pagination=pagination)

@bp.route('analysis/')
def analysis():
    news = News.query.order_by(News.comment_num.desc()).limit(7).all()
    rumors_rank = News.query.order_by(News.like_num.desc()).limit(14).all()

    for rumor in rumors_rank:
        rumor.source = rumor.source.replace('@', '')

    news_by_date = db.session.query(
        cast(News.date, Date).label('date'),
        func.count(News.id).label('count')
    ).group_by(cast(News.date, Date)).all()

    news_count = [ row.count for row in news_by_date]
    news_date = [row.date.strftime('%m-%d') for row in news_by_date]



    return render_template('analysis.html', news=news, rumors_rank=rumors_rank,
                           news_count=news_count, news_date=news_date)

@bp.route('detection/')
def detection():

    return render_template('detection.html', )

@bp.route('about-us/')
def about_us():

    return render_template('about-us.html', )

@bp.route('analysis-refute/')
def analysis_refute():
    news = News.query.order_by(News.comment_num.desc()).limit(7).all()
    rumors_rank = News.query.order_by(News.like_num.desc()).limit(14).all()

    for rumor in rumors_rank:
        rumor.source = rumor.source.replace('@', '')

    news_by_date = db.session.query(
        cast(News.date, Date).label('date'),
        func.count(News.id).label('count')
    ).group_by(cast(News.date, Date)).all()

    news_count = [ row.count for row in news_by_date]
    news_date = [row.date.strftime('%m-%d') for row in news_by_date]


    return render_template('analysis-refute.html',  news=news, rumors_rank=rumors_rank,
                           news_count=news_count, news_date=news_date)

@bp.route('analysis-summary/')
def analysis_summary():

    return render_template('analysis-summary.html', )
