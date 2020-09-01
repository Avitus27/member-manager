import json

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)


@app.errorhandler(404)
def not_found(e):
    return app.response_class(
            response=json.dumps({'error': 'Page Not Found','status': 404}),
            status=404,
            mimetype='application/json'
        )


@app.route('/')
def hello():
    return 'This is a test\n'



