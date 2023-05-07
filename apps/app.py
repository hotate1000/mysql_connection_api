from flask import Flask;
from apps.mysql_connection import views as mysql_connection_views;


def create_app():
    # Flaskクラスをインスタンス化する。
    app = Flask(__name__);
    app.register_blueprint(
        blueprint=mysql_connection_views.mysql_connection,
    )
    return app;