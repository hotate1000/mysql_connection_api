from flask import Blueprint, render_template;


# Blueprint: アプリを分割するためのFlaskの機能
mysql_connection = Blueprint(
    name="mysql_connection",
    import_name=__name__,
    template_folder="templates",
    static_folder="static",
    url_prefix="/mysql_connection",
)


@mysql_connection.route("/")
def index():
    return "Hello World";
