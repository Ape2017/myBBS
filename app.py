from flask import Flask
from config import SECRET_KEY
from routes.index import main as index_routes
from routes.user import main as user_routes
from routes.admin import main as admin_routes
from routes.topic import main as topic_routes
from routes.reply import main as reply_routes
from routes.mail import main as mail_routes


def create_app():
    app = Flask(__name__)
    # 设置 secret_key 以使用 flask 自带的 session
    app.secret_key = SECRET_KEY
    app.register_blueprint(index_routes)
    app.register_blueprint(user_routes, url_prefix='/user')
    app.register_blueprint(admin_routes, url_prefix='/admin')
    app.register_blueprint(topic_routes, url_prefix='/topic')
    app.register_blueprint(reply_routes, url_prefix='/reply')
    app.register_blueprint(mail_routes, url_prefix='/mail')
    # 注册 Jinja2 模板中使用的全局函数 现在用g.user代替了
    # app.jinja_env.globals['current_user'] = current_user
    return app

if __name__ == '__main__':
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=3000,
        threaded=True,
    )
    app = create_app()
    app.run(**config)

