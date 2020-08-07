import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
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
        
    def test_create_appdea(self):
        new_appdea = {
            'name': 'My new app',
            'description': 'My new app in TypeScript'
        }
        res = self.client().post('/appdeas', json=new_appdea)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(data['appdea'])

    def test_get_appdea(self):
        res = self.client().get('/appdeas/1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(data['appdea'])

    def test_delete_appdea(self):
        appdea_to_delete = Appdea.query.order_by(Appdea.id).all()[-1]
        appdea_id = appdea_to_delete.id

        res = self.client().delete(f'/appdeas/{appdea_id}')
        data = json.loads(res.data)

        appdea = Appdea.query.filter_by(id=appdea_id).one_or_none()
        
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(appdea, None)
        

if __name__ == '__main__':
    unittest.main()
