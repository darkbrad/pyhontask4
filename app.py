
from flask import Flask
from blueprint.api import api_blueprint
from blueprint.api.user import user_blueprint
from blueprint.api.items import items_blueprint
from blueprint.pages import pages_blueprint
app=Flask(__name__)
app.register_blueprint(api_blueprint)
app.register_blueprint(user_blueprint)
app.register_blueprint(items_blueprint)
app.register_blueprint(pages_blueprint)


if "__name__"=="__main__":
    app.run()