from flask import Blueprint, render_template, request
from .models import News

# 注意此处蓝图的注册
bp = Blueprint('news', __name__, url_prefix='/news', static_folder='static', template_folder='templates')

# http://127.0.0.1:5000/news/index/

@bp.route('index/')
def index():
    page = request.args.get('page', 1, type=int)
    pagination = News.query.paginate(page=page, per_page=10, error_out=False)
    post_list = pagination.items

    return render_template('index.html', posts=post_list, pagination=pagination)

@bp.route('analysis/')
def analysis():

    return render_template('analysis.html', )

@bp.route('detection/')
def detection():

    return render_template('detection.html', )

@bp.route('about-us/')
def about_us():

    return render_template('about-us.html', )

@bp.route('analysis-refute/')
def analysis_refute():

    return render_template('analysis-refute.html', )

@bp.route('analysis-summary/')
def analysis_summary():

    return render_template('analysis-summary.html', )
