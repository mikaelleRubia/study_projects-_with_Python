from flask import Flask
from .extensions import configuration
from .extensions import admin
from .extensions import appearance
from .extensions import database
from .extensions import auth
from .extensions import commands
from .webui import views


app = Flask(__name__)

configuration.init_app(app)
appearance.init_app(app)
database.init_app(app)
auth.init_app(app)
admin.init_app(app)
commands.init_app(app)
views.init_app(app)
