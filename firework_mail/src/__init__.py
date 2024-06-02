from flask import Flask
from src.config import config_by_name
from src.db import db
from src.scheduler import scheduler
import atexit
from src.mail import mail 



def create_app(config_name: str) -> Flask:
    app = Flask(__name__) 
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    mail.init_app(app)
    scheduler.init_app(app)
    scheduler.start()
    atexit.register(lambda: scheduler.shutdown())

    return app