#!/usr/bin/env python3
"""
Script to run the application using Flask CLI.
"""
import os
from app_factory import AppFactory

# Create application
app = AppFactory.create_app(os.environ.get('FLASK_ENV', 'development'))

if __name__ == "__main__":
    # To use with Flask CLI: flask --app run_app.py run
    print("Use: flask --app run_app.py run")
    print("Or: FLASK_APP=run_app.py flask run")
