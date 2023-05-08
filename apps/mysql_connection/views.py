from flask import Blueprint, render_template;
import pymysql.cursors;
import os;


# Blueprint: アプリを分割するためのFlaskの機能
mysql_connection = Blueprint(
    name="mysql_connection",
    import_name=__name__,
    template_folder="templates",
    static_folder="static",
    url_prefix="/mysql_connection",
)


# mysqlへ接続する
connection = pymysql.connect(
    host="localhost",
    user="root",
    # mysqlのパスワードを入力する。
    password=os.environ.get("MYSQL_PASSWORD"),
    # 操作するデータベース名を入力する。
    db=os.environ.get("MYSQL_DB_NAME"),
    # データを辞書型で渡す。
    cursorclass=pymysql.cursors.DictCursor
)


@mysql_connection.route("/")
def index():
    return "Hello World";


@mysql_connection.route("select")
def select():
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM user;"
            # sqlの実行。
            cursor.execute(sql);
            # 実行したsqlの表示。
            print("\n---実行したsql文---\n", cursor._executed);
            # テーブルデータを取得する。
            db_data = cursor.fetchall();
            print(db_data);
    finally:
        connection.close();
    if db_data:
        return db_data;    
