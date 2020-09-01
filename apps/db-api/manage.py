from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app, db
import os

manager = Manager(app)

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

@manager.command
def runserver(port=5000):
    os.environ["LOG_LEVEL"] = "DEBUG"
    app.run(debug=True, port=int(port))


if __name__ == "__main__":
    manager.run()
