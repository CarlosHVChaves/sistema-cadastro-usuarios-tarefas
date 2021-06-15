from flask import (
    Flask, 
    redirect
)
from flask.config import Config
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_babelex import Babel
from flask_login import (
    LoginManager, 
    login_manager
)


db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    babel = Babel(app)
    app.config.from_object(Config)

    admin = Admin(app, name="Sistema de tarefas", template_mode="bootstrap3")

    db.init_app(app)
    login_manager.init_app(app)

    # Deixar página em português
    @babel.localeselector
    def get_locale():
        # Put your logic here. Application can store locale in
        # user profile, cookie, session, etc.
        return 'pt'

    # Página de Registro admin
    import admin as administrator
    administrator.init_app(admin)

    @app.route("/")
    def index():
        return redirect("/admin/usuário")

    return app
