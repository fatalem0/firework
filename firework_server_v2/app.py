import os
import flask

flask.helpers._endpoint_from_view_func = (
    flask.sansio.scaffold._endpoint_from_view_func
)  # monkey patch https://github.com/python-restx/flask-restx/issues/567. @basekeet
from flask_migrate import Migrate
from src import blueprint, create_app, db
from commands import tests

app = create_app(os.getenv("BOILERPLATE_ENV") or "dev")

app.register_blueprint(blueprint)
app.register_blueprint(tests)
migrate = Migrate(app, db)

app.app_context().push()

if __name__ == "__main__":
    app.run(host="0.0.0.0")
