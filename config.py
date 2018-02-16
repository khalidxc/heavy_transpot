
db_host = 'localhost'
db_username = 'heavy_transpot'
db_password = '6116'
db_name = 'heavy_transpot'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'dfvkjvnkjsvnjfnmomfnasfioreajfvoermyowetfuwrgfpmfgcxajsvijiou3e'

########################################## DO NOT TOUCH BELOW THIS LINE ##########################################
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import sys

# sys.path.insert(0, '/var/www/app.swe363.ml/test/')

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://%s:%s@%s/%s?charset=utf8' % (db_username, db_password, db_host, db_name)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
app.config['SECRET_KEY'] = SECRET_KEY

db = SQLAlchemy(app)    # initialize app in the SQLAlchemy instance

login_manager = LoginManager()
login_manager.init_app(app)
