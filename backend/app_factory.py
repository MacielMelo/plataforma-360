"""
Factory for Flask application creation.
"""
from flask import Flask
from typing import Optional

from config.config import get_config
from blueprints.hello_world_blueprint import HelloWorldBlueprint


class AppFactory:
    """Factory for Flask application creation and configuration."""
    
    @staticmethod
    def create_app(environment: str = 'default') -> Flask:
        """
        Creates and configures a Flask application instance.
        
        Args:
            environment: Configuration environment (development, production, testing)
            
        Returns:
            Configured Flask application instance
        """
        app = Flask(__name__)
        
        # Load configurations
        config = get_config(environment)
        app.config.update(config.get_config())
        
        # Register blueprints
        AppFactory._register_blueprints(app)
        
        # Register error handlers
        AppFactory._register_error_handlers(app)
        
        return app
    
    @staticmethod
    def _register_blueprints(app: Flask) -> None:
        """
        Registers blueprints in the application.
        
        Args:
            app: Flask application instance
        """
        # Hello World Blueprint
        hello_world_bp = HelloWorldBlueprint()
        app.register_blueprint(hello_world_bp.get_blueprint())
    
    @staticmethod
    def _register_error_handlers(app: Flask) -> None:
        """
        Registers global error handlers.
        
        Args:
            app: Flask application instance
        """
        @app.errorhandler(404)
        def not_found(error):
            return {"error": "Endpoint not found"}, 404
        
        @app.errorhandler(500)
        def internal_error(error):
            return {"error": "Internal server error"}, 500
        
        @app.errorhandler(400)
        def bad_request(error):
            return {"error": "Bad request"}, 400
