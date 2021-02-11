import json
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['DEBUG'] = True
app.config['TESTING'] = True
app.config['CSRF_ENABLED'] = True
app.config['SECRET_KEY'] = "u=M~[bf5bM0f2]m)_TsZjL[63+l{K~Z&j^DX|\\T;0.>1LzdP%Y=_^:ZIL*A*9,1l9oR.'SL(~{&;:o?$S,(x!|$W0`{my./)-5e3?NOA6EOxf103'8(CQG79je4-Yo%"
# TODO: Fix above so that this is pulled from .env
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from models import *

@app.errorhandler(404)
def not_found(e):
    return app.response_class(
        response=json.dumps({'error': 'Page Not Found', 'status': 404}),
        status=404,
        mimetype='application/json'
    )


@app.route('/')
def hello():
    return 'This is a test\n'
