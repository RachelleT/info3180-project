from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "change this to be a more random key"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://project1:project1@localhost/project1"
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://ajylilsknyxcfn:979a702b69261dc933ae2a0af77ceab6d0e6e90681d516ed0df9fbe82ef13649@ec2-54-225-95-183.compute-1.amazonaws.com:5432/ddhqh8ha1b8c9r"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
UPLOAD_FOLDER = './app/static/uploads'

db = SQLAlchemy(app)

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config.from_object(__name__)
from app import views
