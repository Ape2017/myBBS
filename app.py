from flask import Flask
from routes.index import main as index_routes
from routes.user import main as user_routes
from routes.admin import main as admin_routes
from routes.topic import main as topic_routes
from routes.reply import main as reply_routes


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    app.register_blueprint(index_routes)
    app.register_blueprint(user_routes, url_prefix='/user')
    app.register_blueprint(admin_routes, url_prefix='/admin')
    app.register_blueprint(topic_routes, url_prefix='/topic')
    app.register_blueprint(reply_routes, url_prefix='/reply')
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

