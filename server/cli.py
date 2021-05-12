from werkzeug.wsgi import DispatcherMiddleware
from api import auth, user


def create_app(settings=None):
    app = DispatcherMiddleware(
        auth.create_app(settings),
        {
            '/user': user.create_app(settings),
        },
    )

    return app