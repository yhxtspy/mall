import os
from dotenv import load_dotenv

# from api import create_app
from flask_sqlalchemy import SQLAlchemy
from werkzeug.serving import run_simple

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)




import sys
import click
from flask_migrate import Migrate, upgrade
from factory import create_app
# from app.models import User, Follow, Role, Permission, Post, Comment
db = SQLAlchemy()
app = create_app()
# manager = Manager(app)
migrate = Migrate(app, db)


# def make_shell_context():
#     return dict(app=app, db=db, User=User, Role=Role)


# manager.add_command('shell', Shell(make_context=make_shell_context))
# manager.add_command('db', MigrateCommand)
# manager.add_command('runserver', Server(host="0.0.0.0"))



if __name__ == '__main__':
    run_simple(
        '10.19.201.9',
        20001,
        app,
        threaded=True,
        use_reloader=True,
        use_debugger=True)
