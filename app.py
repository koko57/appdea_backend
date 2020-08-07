import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db
from controllers.appdeas import appdeas
from flask_script import Manager
from flask_migrate import MigrateCommand

def create_app(test_config=None):
    flask_app = Flask(__name__)
    flask_app.register_blueprint(appdeas)
    CORS(flask_app)
    setup_db(flask_app)



    return flask_app

APP = create_app()
manager = Manager(APP)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)
