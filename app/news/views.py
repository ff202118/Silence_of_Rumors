from flask import Blueprint, render_template

# 注意此处蓝图的注册
bp = Blueprint('news', __name__, url_prefix='/news', static_folder='static', template_folder='templates')

# http://127.0.0.1:5000/news/index/

@bp.route('index/')
def index():
    posts = [1, 2, 3, 4, 5]
    return render_template('index.html', posts=posts)
