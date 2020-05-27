
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db
from controllers.appdeas import appdeas

def create_app(test_config=None):
    app = Flask(__name__)
    app.register_blueprint(appdeas)
    CORS(app)
    setup_db(app)

    @app.route('/')
    def hello():
        return 'Hello, World!'

    return app

flask_app = create_app()

if __name__ == '__main__':
    flask_app.run(host='0.0.0.0', port=8080, debug=True)
