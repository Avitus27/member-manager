from flask_script import Manager
from app import app
import os

manager = Manager(app)

@manager.command
def runserver(port=5000):
    os.environ["LOG_LEVEL"] = "DEBUG"
    app.run(debug=True, port=int(port))

if __name__ == "__main__":
    manager.run()

