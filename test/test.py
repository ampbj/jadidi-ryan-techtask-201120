import sys
sys.path.append('..')
import unittest
from app import app



class LunchAppTest(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.app = app.test_client()
        self.assertEqual(app.debug, False)

    def testLunchEndpoint(self):
        result = self.app.get('/lunch')
        self.assertEqual(result.status_code, 200)

    def testHomeEndpoint(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 302)


if __name__ == '__main__':
    unittest.main()
