
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

def create_app(test_config=None):
    app = Flask(__name__)
    CORS(app)

    @app.route('/')
    def hello():
        return 'Hello, World!'

    return app

flask_app = create_app()

if __name__ == '__main__':
    flask_app.run(host='0.0.0.0', port=8080, debug=True)
