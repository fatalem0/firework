import os

basedir = os.path.abspath(os.path.dirname(__file__))

local_base = os.environ.get("DATABASE_URL") or "sqlite:///" + os.path.join(
    basedir, "flask_boilerplate_main.db"
)


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "my_precious_secret_key")
    DEBUG = False
    # Swagger
    RESTX_MASK_SWAGGER = False


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = local_base
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(
        basedir, "flask_boilerplate_test.db"
    )
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = local_base


config_by_name = dict(dev=DevelopmentConfig, test=TestingConfig, prod=ProductionConfig)

key = Config.SECRET_KEY
