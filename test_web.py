from flask import Flask, Request, request
import unittest
from io import BytesIO

from main import app

class FlaskTest(unittest.TestCase):

    def setUp(self):
        """Set up test application client"""
        self.app = app.test_client() 
        self.app.testing = True

    def test_home_status_code(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_post_request(self):
        """Assert that user is redirected with status 302 after creating a todo item"""
        data = dict(
            file=(BytesIO(b'my file contents'), "file.txt")
        )
        response = self.app.post('/', content_type='multipart/form-data',
                                 data=data
                                 )
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
