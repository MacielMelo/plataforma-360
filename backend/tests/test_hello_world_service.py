"""
Tests for the HelloWorldService.
"""
import unittest
from services.hello_world_service import HelloWorldService


class TestHelloWorldService(unittest.TestCase):
    """Tests for the HelloWorldService."""
    
    def setUp(self):
        """Setup before each test."""
        self.service = HelloWorldService()
    
    def test_process_default_greeting(self):
        """Tests processing with default greeting."""
        result = self.service.process()
        self.assertEqual(result, {"message": "Hello, World!"})
    
    def test_process_with_name(self):
        """Tests processing with custom name."""
        data = {"name": "Python"}
        result = self.service.process(data)
        self.assertEqual(result, {"message": "Hello, Python!!"})
    
    def test_set_and_get_greeting(self):
        """Tests setting and getting custom greeting."""
        new_greeting = "Hi, World!"
        self.service.set_greeting(new_greeting)
        self.assertEqual(self.service.get_greeting(), new_greeting)
    
    def test_custom_greeting_with_name(self):
        """Tests custom greeting with name."""
        self.service.set_greeting("Hi, World")
        data = {"name": "Flask"}
        result = self.service.process(data)
        self.assertEqual(result, {"message": "Hi, Flask!"})


if __name__ == '__main__':
    unittest.main()
