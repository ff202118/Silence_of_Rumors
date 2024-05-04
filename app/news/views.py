from datetime import datetime, timedelta
from flask import Blueprint, render_template, request
from .models import News, Rumors, Refute, Category, Follows
from .utils import get_news_data, get_post_list, get_weight
from project import db
from sqlalchemy import cast, Date
from ..user.views import login_required

# 注意此处蓝图的注册
bp = Blueprint('news', __name__, url_prefix='/news', static_folder='static', template_folder='templates')

# http://127.0.0.1:5000/news/index/


@bp.route('index/rate/<string:rate_cate>')
def rate(rate_cate):
    page = request.args.get('page', 1, type=int)
    if rate_cate == 'high':
        pagination = News.query.filter(News.rate >= 70).order_by(News.rate.desc()).paginate(page=page, per_page=10, error_out=False)
    elif rate_cate == 'mid':
        pagination = News.query.filter(News.rate >= 50, 70 > News.rate).order_by(News.rate.desc()).paginate(page=page, per_page=10, error_out=False)
    else:
        pagination = News.query.filter(News.rate < 50).order_by(News.rate.desc()).paginate(page=page, per_page=10, error_out=False)

    post_list = pagination.items

    return render_template('rate_list.html', posts=post_list, pagination=pagination, rt=rate_cate)

@bp.route('index/publisher/<string:pub>')
def publisher(pub):
    page = request.args.get('page', 1, type=int)
    if pub == 'authority':
        pagination = News.query.filter(News.authority != None).paginate(page=page, per_page=10, error_out=False)
    else:
        pagination = News.query.filter(News.authority.is_(None)).paginate(page=page, per_page=10, error_out=False)

    post_list = pagination.items

    return render_template('publisher_list.html', posts=post_list, pagination=pagination, pub=pub)

@bp.route('index/time/<int:t>')
def time(t):
    page = request.args.get('page', 1, type=int)

    current_time = datetime.now()
    days_ago = current_time - timedelta(days=t)

    pagination = News.query.filter(days_ago <= cast(News.date, Date)).order_by(News.date.desc()).paginate(page=page, per_page=10, error_out=False)
    post_list = pagination.items

    return render_template('time_list.html', posts=post_list, pagination=pagination, t=t)

@bp.route('index/search/<string:content>')
def search(content):
    page = request.args.get('page', 1, type=int)

    print(content, '------------------------')
    pagination = News.query.filter(News.content.like(f'%{content}%')).paginate(page=page, per_page=10, error_out=False)
    post_list = pagination.items

    return render_template('search_list.html', posts=post_list, pagination=pagination, content=content)

@bp.route('index/popular')
def popular():
    page = request.args.get('page', 1, type=int)
    pagination = News.query.order_by(News.like_num.desc(), News.date.desc()).paginate(page=page, per_page=10, error_out=False)

    post_list = pagination.items

    for post in post_list:
        if post.authority != None :
            post.authority = post.authority.replace('@', '')

    return render_template('popular.html', posts=post_list, pagination=pagination)


@bp.route('index/category/<string:cate>')
def category(cate):
    page = request.args.get('page', 1, type=int)

    Type = Category.query.filter(Category.name==cate).first()
    print(type(Type))

    pagination = News.query.filter(News.category_id==Type.id).order_by(News.date.desc()).paginate(page=page, per_page=10, error_out=False)

    post_list = pagination.items

    for post in post_list:
        if post.authority != None :
            post.authority = post.authority.replace('@', '')

    return render_template('category.html', posts=post_list, pagination=pagination, cate=cate)


@login_required
@bp.route('index/')
def index():
    page = request.args.get('page', 1, type=int)
    pagination = News.query.order_by(News.date.desc()).paginate(page=page, per_page=10, error_out=False)

    post_list = pagination.items

    for post in post_list:
        if post.authority != None :
            post.authority = post.authority.replace('@', '')

    return render_template('index.html', posts=post_list, pagination=pagination)

@bp.route('analysis/')
def analysis():
    news = Rumors.query.order_by(Rumors.comment_num.desc()).limit(7).all()

    source_counts = db.session.query(Rumors.source, Rumors.source_url, db.func.count(Rumors.id)). \
        group_by(Rumors.source, Rumors.source_url).order_by(db.func.count(Rumors.id).desc()).limit(12).all()

    rumors_rank = []
    for item in source_counts:
        Dict = {}
        Dict['source'] = item[0].replace('@', '')
        Dict['source_url'] = item[1]
        Dict['counts'] = item[2]
        rumors_rank.append(Dict)

    print(rumors_rank[:2])


    news_date, news_count = get_news_data(Rumors)

    word_weight = get_weight('rumor')

    # 查询各个类别下的辟谣信息数量
    rumors_counts = db.session.query(Category.name, db.func.count(Rumors.id)). \
        join(Category.rumors).group_by(Category.name).all()

    # 将结果组合成字典
    counts = {name:  refute_count for
              name, refute_count in rumors_counts}

    return render_template('analysis.html', news=news, rumors_rank=rumors_rank,
                           news_count=news_count, news_date=news_date, word_weight=word_weight, counts=counts)


@bp.route('rumors_follow/')
def rumors_follow():
    page = request.args.get('page', 1, type=int)
    pagination = Follows.query.paginate(page=page, per_page=10, error_out=False)

    post_list = pagination.items

    Post_list = get_post_list(post_list)


    return render_template('rumors_follow.html', posts=Post_list, pagination=pagination)


@bp.route('about-us/')
def about_us():

    return render_template('about-us.html', )


@bp.route('analysis-refute/')
def analysis_refute():
    news = Refute.query.order_by(Refute.comment_num.desc()).limit(7).all()

    source_counts = db.session.query(Refute.source, Refute.source_url, db.func.count(Refute.id)). \
        group_by(Refute.source, Refute.source_url).order_by(db.func.count(Refute.id).desc()).limit(12).all()

    rumors_rank = []
    for item in source_counts:
        Dict = {}
        Dict['source'] = item[0].replace('@', '')
        Dict['source_url'] = item[1]
        Dict['counts'] = item[2]
        rumors_rank.append(Dict)

    news_date, news_count = get_news_data(Refute)

    word_weight = get_weight('refute')

    # 查询各个类别下的辟谣信息数量
    refute_counts = db.session.query(Category.name, db.func.count(Refute.id)). \
        join(Category.refute).group_by(Category.name).all()

    # 将结果组合成字典
    counts = {name:  refute_count for
              name, refute_count in refute_counts}

    return render_template('analysis-refute.html',  news=news, rumors_rank=rumors_rank,
                           news_count=news_count, news_date=news_date, word_weight=word_weight, counts=counts)

@bp.route('analysis-summary/')
def analysis_summary():

    news1 = Rumors.query.order_by(Rumors.comment_num.desc()).limit(12).all()
    news2 = Refute.query.order_by(Refute.comment_num.desc()).limit(12).all()

    source_counts = db.session.query(Rumors.source, Rumors.source_url, db.func.count(Rumors.id)). \
        group_by(Rumors.source, Rumors.source_url).order_by(db.func.count(Rumors.id).desc()).limit(12).all()

    rumors_rank = []
    for item in source_counts:
        Dict = {}
        Dict['source'] = item[0].replace('@', '')
        Dict['source_url'] = item[1]
        Dict['counts'] = item[2]
        rumors_rank.append(Dict)



    source_counts = db.session.query(Refute.source, Refute.source_url, db.func.count(Refute.id)). \
        group_by(Refute.source, Refute.source_url).order_by(db.func.count(Refute.id).desc()).limit(12).all()
    refute_rank = []
    for item in source_counts:
        Dict = {}
        Dict['source'] = item[0].replace('@', '')
        Dict['source_url'] = item[1]
        Dict['counts'] = item[2]
        refute_rank.append(Dict)

    news_date1, news_count1 = get_news_data(Rumors)
    news_date2, news_count2 = get_news_data(Refute)

    word_weight = get_weight('refute')

    return render_template('analysis-summary.html', news=news1, rumors_rank=rumors_rank,
                           news_count1=news_count1, news_date1=news_date1, news2=news2, refute_rank=refute_rank,
                           news_count2=news_count2, news_date2=news_date2, word_weight=word_weight)
