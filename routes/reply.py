from flask import (
    render_template,
    request,
    redirect,
    Blueprint,
    flash,
    g,
    abort,
)
from models.topic import Topic
from models.reply import Reply
from routes.mail import inform_users
from auth import (
    login_required,
    author_or_admin_required,
    token_required,
)

main = Blueprint('reply', __name__)


@main.route('/add', methods=["POST"])
@login_required
@token_required
def add():
    u = g.user
    form = request.form
    r = Reply.new(form, user_id=u.id)
    Topic.replied(r)
    inform_users(form.get('content'), request.referrer)
    return redirect(request.referrer)


@main.route("/edit/<int:r_id>")
@login_required
def edit(r_id):
    r = Reply.find_by(id=r_id)
    if r is None:
        abort(404)
    else:
        return render_template('reply/edit.html', reply=r)


@main.route("/update", methods=["POST"])
@login_required
@author_or_admin_required
@token_required
def update():
    form = request.form
    r_id = int(form.get('id'))
    r = Reply.find_by(id=r_id)
    r.update_reply(form)
    flash('修改回复成功', 'success')
    return redirect(form.get('next'))


@main.route("/delete")
@login_required
@author_or_admin_required
@token_required
def delete():
    r_id = int(request.args.get('id'))
    r = Reply.find_by(id=r_id)
    r.delete()
    flash('删除回复成功', 'success')
    return redirect(request.referrer)
