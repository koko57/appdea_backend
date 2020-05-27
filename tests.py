import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Appdea


class AppdeaTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.db_path = f'{os.environ["DATABASE_URL"]}_test'
        setup_db(self.app, self.db_path)

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()

    def tearDown(self):
        pass

    def test_get_appdeas(self):
        res = self.client().get('/appdeas')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(data['appdeas'])
        self.assertTrue(data['results_count'])


if __name__ == '__main__':
    unittest.main()
