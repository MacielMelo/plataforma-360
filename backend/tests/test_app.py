"""
Tests for the Flask application.
"""
import unittest
import json
from app_factory import AppFactory


class TestApp(unittest.TestCase):
    """Integration tests for the application."""
    
    def setUp(self):
        """Setup before each test."""
        self.app = AppFactory.create_app('testing')
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
    
    def tearDown(self):
        """Cleanup after each test."""
        self.app_context.pop()
    
    def test_hello_world_endpoint(self):
        """Tests the basic greeting endpoint."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        self.assertEqual(data, {"message": "Hello, World!"})
    
    def test_hello_name_endpoint(self):
        """Tests the greeting endpoint with name."""
        response = self.client.get('/hello/Flask')
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        self.assertEqual(data, {"message": "Hello, Flask!!"})
    
    def test_update_greeting_endpoint(self):
        """Tests the greeting update endpoint."""
        greeting_data = {"greeting": "Hi, World!"}
        response = self.client.post(
            '/greeting',
            data=json.dumps(greeting_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        self.assertEqual(data, {"message": "Greeting updated successfully"})
    
    def test_update_greeting_missing_field(self):
        """Tests greeting update without required field."""
        response = self.client.post(
            '/greeting',
            data=json.dumps({}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        
        data = json.loads(response.data)
        self.assertIn("error", data)
    
    def test_not_found_endpoint(self):
        """Tests non-existent endpoint."""
        response = self.client.get('/nonexistent')
        self.assertEqual(response.status_code, 404)
        
        data = json.loads(response.data)
        self.assertEqual(data, {"error": "Endpoint not found"})


if __name__ == '__main__':
    unittest.main()
