from flask import Flask
from flask_bcrypt import Bcrypt
from flask_apscheduler import APScheduler

app = Flask(__name__)
bcrypt = Bcrypt(app)
scheduler = APScheduler()
from project.storage.db import DB
db = DB()

from flask_login import LoginManager
login_manager = LoginManager(app)
