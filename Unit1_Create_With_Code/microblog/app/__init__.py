# initilisation file

from flask import Flask
from config import Config

app = Flask(__name__)  # create instance
app.config.from_object(Config)

from app import routes  # imports routes from the instance
