import os


class Config:
    @staticmethod
    def init_app(app):
        pass
basedir = os.path.abspath(os.path.dirname(__file__))

class DevelopmentConfig(Config):
    DEBUG = True
    ASSETS_DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL',
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite'))

    @classmethod
    def init_app(cls, app):
        print('THIS APP IS IN DEBUG MODE. \
                YOU SHOULD NOT SEE THIS IN PRODUCTION.')

config = {
    'development': DevelopmentConfig,
    # 'development': DevelopmentConfig,
    # 'testing': TestingConfig,
    # 'production': ProductionConfig,
    # 'default': DevelopmentConfig,
    # 'heroku': HerokuConfig,
    # 'unix': UnixConfig
}