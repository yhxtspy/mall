import importlib
import os
import pkgutil

from flask import Flask, Blueprint
from flask_cors import CORS

from config import Config, config as _config

cors = CORS()

def create_app(settings_override=None):
    app = Flask(__name__)
    cfg = _config[app.env]
    app.config.from_object(cfg)
    cfg.init_app(app)
    app.config.from_object(settings_override)

    app.config.from_object(_config[app.env])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # not using sqlalchemy event system, hence disabling it

    _config[app.env].init_app(app)
    cors.init_app(app)


    from api import home as home_blueprint
    app.register_blueprint(home_blueprint)
    from api.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    from api.user import user as user_blueprint
    app.register_blueprint(user_blueprint)
    return app


def register_blueprints(app, package_name, package_path):
    """注册包下的蓝图模块

    :param app: Flask app
    :param package_name: the package name
    :param package_path: the package path
    """

    rv = []
    for _, name, _ in pkgutil.iter_modules(package_path):
        m = importlib.import_module('%s.%s' % (package_name, name))
        for item in dir(m):
            item = getattr(m, item)
            if isinstance(item, Blueprint):
                app.register_blueprint(item)
            rv.append(item)
    return rv
