from flask import (
    render_template,
    Blueprint,
    request,
    g,
    redirect,
    session,
)
from models.board import Board
from models.topic import Topic
from auth import current_user
from config import DOMAIN_NAME

main = Blueprint('index', __name__)


@main.before_app_request
def before_request():
    """
    每次请求之前把g.user设为当前用户
    """
    g.user = current_user()


@main.route('/')
def index():
    page = int(request.args.get('page', 1))
    bs = Board.find_all()
    b_id = int(request.args.get('board_id', -1))
    if b_id == -1:
        pages = Topic.pages()
        ts = Topic.find_page(page=page, __sort=['updated_time', -1])
    else:
        pages = Topic.pages(board_id=b_id)
        ts = Topic.find_page(page=page, board_id=b_id, __sort=['updated_time', -1])
    return render_template('index.html', bs=bs, ts=ts, b_id=b_id, page=page, pages=pages)


@main.route('/login')
def login():
    return render_template('user/login.html')


@main.route('/register')
def register():
    return render_template('user/register.html')


@main.route("/search")
def search():
    query = request.args.get('query')
    # host = request.headers.get('Host')
    host = DOMAIN_NAME
    google_search = 'https://www.google.com/search?q=site:{} {}'
    google_search = google_search.format(host, query)
    return redirect(google_search)


@main.route("/theme/<string:theme>")
def change_theme(theme):
    session['theme'] = theme
    return redirect(request.referrer)

