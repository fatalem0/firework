import os


basedir =  os.path.abspath(os.path.join(
    os.path.join(
        __file__ ,"../../.."
    ), os.environ.get("LOCAL_BASE")
))

local_base = os.environ.get("DATABASE_URL") if os.environ.get("DATABASE_URL") else "sqlite:///" + os.path.join(
        basedir, "flask_boilerplate_main.db"
    )

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "my_precious_secret_key")
    DEBUG = False
    # Scheduler
    SCHEDULER_API_ENABLED = True
    # Swagger
    RESTX_MASK_SWAGGER = False
    # Mail
    MAIL_SERVER = os.environ.get("MAIL_SERVER")
    MAIL_PORT = os.environ.get("MAIL_PORT")
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    MAIL_USE_TLS = True


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = local_base
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = local_base


config_by_name = dict(dev=DevelopmentConfig, prod=ProductionConfig)

key = Config.SECRET_KEY
