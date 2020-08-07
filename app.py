import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db
from controllers.appdeas import appdeas

def create_app(test_config=None):
    flask_app = Flask(__name__)
    flask_app.register_blueprint(appdeas)
    CORS(flask_app)
    setup_db(flask_app)

    return flask_app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
