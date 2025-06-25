"""
Hello World Controller (maintained for compatibility).
This file is being deprecated in favor of blueprints.
"""
from abc import ABC, abstractmethod
from flask import Flask, jsonify
from typing import Dict, Any

from services.hello_world_service import HelloWorldService


class BaseController(ABC):
    """Abstract base class for controllers."""
    
    def __init__(self, service: Any = None):
        """
        Initializes the controller.
        
        Args:
            service: Service associated with the controller
        """
        self.service = service
    
    @abstractmethod
    def register_routes(self, app: Flask) -> None:
        """Registers routes in the Flask app."""
        pass


class HelloWorldController(BaseController):
    """Controller for Hello World endpoints."""
    
    def __init__(self):
        """Initializes the controller with the appropriate service."""
        super().__init__(HelloWorldService())
    
    def register_routes(self, app: Flask) -> None:
        """
        Registers Hello World routes.
        
        Args:
            app: Flask application instance
        """
        app.add_url_rule('/', 'hello_world', self.hello_world, methods=['GET'])
    
    def hello_world(self) -> Dict[str, Any]:
        """
        Basic greeting endpoint.
        
        Returns:
            JSON response with the message
        """
        try:
            result = self.service.process()
            return jsonify(result)
        except Exception as e:
            return jsonify({"error": str(e)})


def init_routes(app: Flask) -> None:
    """
    Compatibility function to initialize routes.
    
    Args:
        app: Flask application instance
    """
    controller = HelloWorldController()
    controller.register_routes(app)