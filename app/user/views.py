import functools

from .models import User
from flask import Blueprint, flash, render_template, request, redirect, url_for, session, g
from werkzeug.security import check_password_hash, generate_password_hash
from project import db
import re

# 注意此处蓝图的注册
bp = Blueprint('user', __name__, url_prefix='/user', static_folder='static', template_folder='templates')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    error = ""
    # 登录视图
    if request.method == "POST":
        result = request.form
        username = result['username']
        password = result['password']

        user = User.query.filter_by(username=username).first()
        if user is not None and check_password_hash(user.password, password):
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('news.index'))
        else:
            error = "用户名或密码错误 !"

    return render_template('login.html', error=error)


@bp.route('/register', methods=['GET', 'POST'])
def register():

    error = ""
    # 登录视图
    if request.method == "POST":
        result = request.form
        username = result['username']
        password = result['password']
        email = result['email']

        print(username, password)
        user = User.query.filter_by(username=username).first()

        match1 = re.match('^[a-zA-Z0-9_]{3,20}$', username)
        match2 = re.match('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', password)

        # Admin202118  @Admin202118
        if not match1:
            error = "用户名应该由字母、数字和下划线组成，并且长度在3到20个字符之间 !"
        elif not match2:
            error = "密码应该至少包含8个字符，并且至少包含一个大写字母、一个小写字母、一个数字和一个特殊字符 !"
        elif user is not None:
            error = "用户名已存在 !"
        else:
            user = User(username=username, password=generate_password_hash(password), email=email)
            db.session.add(user)
            db.session.commit()
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('news.index'))

    return render_template('login.html', error=error)

@bp.route('/logout')
def logout():
    # 注销
    session.clear()
    return redirect(url_for('user.login'))

@bp.before_app_request
def load_logged_in_user():
    # 每个请求之前都回去session中查看user_id来获取用户
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(int(user_id))

def login_required(view):
    # 限制必须登录才能访问的页面装饰器
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('user.login'))
        return view(**kwargs)
    return wrapped_view
