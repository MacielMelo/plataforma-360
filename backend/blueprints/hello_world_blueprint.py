"""
Blueprint for Hello World routes.
"""
from flask import Blueprint, jsonify, request
from typing import Tuple, Dict, Any

from services.hello_world_service import HelloWorldService


class HelloWorldBlueprint:
    """Class to manage the Hello World blueprint."""
    
    def __init__(self, name: str = 'hello_world', url_prefix: str = '/'):
        """
        Initializes the blueprint.
        
        Args:
            name: Blueprint name
            url_prefix: URL prefix
        """
        self.blueprint = Blueprint(name, __name__, url_prefix=url_prefix)
        self.service = HelloWorldService()
        self._register_routes()
    
    def _register_routes(self) -> None:
        """Registers the blueprint routes."""
        self.blueprint.add_url_rule(
            '/',
            'hello_world',
            self._hello_world,
            methods=['GET']
        )
        
        self.blueprint.add_url_rule(
            '/hello/<name>',
            'hello_name',
            self._hello_name,
            methods=['GET']
        )
        
        self.blueprint.add_url_rule(
            '/greeting',
            'update_greeting',
            self._update_greeting,
            methods=['POST']
        )
    
    def _hello_world(self) -> Tuple[Dict[str, Any], int]:
        """
        Basic greeting endpoint.
        
        Returns:
            Tuple with JSON response and status code
        """
        try:
            result = self.service.process()
            return jsonify(result), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    def _hello_name(self, name: str) -> Tuple[Dict[str, Any], int]:
        """
        Personalized greeting endpoint.
        
        Args:
            name: Name to personalize the greeting
            
        Returns:
            Tuple with JSON response and status code
        """
        try:
            result = self.service.process({"name": name})
            return jsonify(result), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    def _update_greeting(self) -> Tuple[Dict[str, Any], int]:
        """
        Endpoint to update the greeting message.
        
        Returns:
            Tuple with JSON response and status code
        """
        try:
            data = request.get_json()
            if not data or 'greeting' not in data:
                return jsonify({"error": "Field 'greeting' is required"}), 400
            
            self.service.set_greeting(data['greeting'])
            return jsonify({"message": "Greeting updated successfully"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    def get_blueprint(self) -> Blueprint:
        """
        Returns the configured blueprint.
        
        Returns:
            Flask Blueprint
        """
        return self.blueprint
