from flask import Flask
from flask_login import LoginManager, current_user
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate(compare_type=True)
login_manager = LoginManager()


def create_app():
    # initialize flask app
    app = Flask(__name__)
    # import all settings from settings.py
    app.config.from_pyfile("settings.py")

    # initialize sqlalchemy
    db.init_app(app)
    # initialize flask migrate
    migrate.init_app(app, db)
    # initialize flask login
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    # define index route
    @app.route("/", methods=["GET"])
    def index():
        return "index"

    # TODO: input controller here
    # from app.controllers import auth
    # app.register_blueprint(auth.bp)

    # error handler controller
    from app.controllers import error_handler

    app.register_blueprint(error_handler.bp)

    # TODO: input command
    # from app.commands.user import user_cli
    # app.cli.add_command(user_cli)

    return app


# import models to enable flask migration
from app import models
