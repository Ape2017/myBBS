from flask import (
    render_template,
    request,
    redirect,
    url_for,
    Blueprint,
    flash,
)
from models.board import Board
from models.user import User
from auth import (
    login_required,
    admin_required,
    token_required,
)

main = Blueprint('admin', __name__)


@main.route('/')
@login_required
@admin_required
def index():
    return render_template('admin.html')


@main.route('/board/add', methods=['Post'])
@login_required
@admin_required
@token_required
def add_board():
    form = request.form
    Board.new(form)
    flash('添加板块成功', 'success')
    return redirect(url_for('admin.index'))


@main.route('/admin/add', methods=['Post'])
@login_required
@admin_required
@token_required
def add_admin():
    form = request.form
    if User.add_admin(form):
        flash('添加管理员成功', 'success')
    else:
        flash('添加管理员失败，用户不存在', 'error')
    return redirect(url_for('admin.index'))


@main.route('/user/delete', methods=['Post'])
@login_required
@admin_required
@token_required
def delete_user():
    username = request.form.get('username')
    u = User.find_by(username=username)
    if u is None:
        flash('删除用户失败，用户名不存在', 'error')
    elif u.admin is True:
        flash('删除用户失败，该用户是管理员', 'error')
    else:
        u.delete()
        flash('删除用户成功', 'success')
    return redirect(url_for('admin.index'))
