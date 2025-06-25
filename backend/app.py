"""
Application entry point.
"""
import os
from app_factory import AppFactory


def main() -> None:
    """Main function to start the application."""
    # Get environment from environment variables
    environment = os.environ.get('FLASK_ENV', 'development')
    
    # Create application using factory
    app = AppFactory.create_app(environment)
    
    # Start server
    app.run(
        debug=app.config.get('DEBUG', False),
        host=os.environ.get('HOST', '127.0.0.1'),
        port=int(os.environ.get('PORT', 5000))
    )


if __name__ == "__main__":
    main()