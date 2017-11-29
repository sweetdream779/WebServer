from flask import Flask, Request, request, url_for
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

    def test_compare_status_code(self):
        result = self.app.get('/compare')
        self.assertEqual(result.status_code, 200)

    def test_count_status_code(self):
        result = self.app.get('/count')
        self.assertEqual(result.status_code, 200)


    def test_post_count_request(self):
        """Assert that user is redirected with status 302 after creating a todo item"""
        data = dict(
            file=(BytesIO(b'my file contents'), "file.txt")
        )
        response = self.app.post('/count/result', content_type='multipart/form-data',
                                 data=data
                                 )
        self.assertEqual(response.status_code, 200)

    def test_post_count_one_request(self):
        """Assert that user is redirected with status 302 after creating a todo item"""
        data = dict(
            file=(BytesIO(b'contents'), "file.txt")
        )
        response = self.app.post('/count/result', content_type='multipart/form-data',
                                 data=data
                                 )
        self.assertEqual(response.status_code, 200)

    def test_empty_post_count_request(self):
        """Assert that user is redirected with status 302 after creating a todo item"""

        response = self.app.post('/count/result', content_type='multipart/form-data',
                                 data="", follow_redirects=True
                                 )
        
    def test_post_compare_request(self):
        """Assert that user is redirected with status 302 after creating a todo item"""
        data = dict(
            file1=(BytesIO(b'my file contents'), "file1.txt"),
            file2=(BytesIO(b'my file'), "file2.txt")
        )
        response = self.app.post('/compare/result', content_type='multipart/form-data',
                                 data=data
                                 )
        self.assertEqual(response.status_code, 200)

    def test_empty_post_compare_request(self):
        """Assert that user is redirected with status 302 after creating a todo item"""
        data = dict(
            file1="",
            file2=""
        )
        response = self.app.post('/compare/result', content_type='multipart/form-data',
                                 data=data, follow_redirects=True
                                 )

if __name__ == '__main__':
    unittest.main()
