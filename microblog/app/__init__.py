from flask import Flask

app = Flask(__name__, static_folder='static')
print(__name__)

from app import routes
