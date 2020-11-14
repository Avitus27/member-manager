from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'This is a test. Testing 123\n'
