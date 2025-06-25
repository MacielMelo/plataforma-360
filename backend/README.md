# Platform 360 - Backend

This project has been refactored to follow Object-Oriented Programming principles and Python best practices.

## 🏗️ Architecture

The application follows a layered architecture with clear separation of responsibilities:

```
backend/
├── app.py                      # Application entry point
├── app_factory.py             # Factory for Flask app creation
├── requirements.txt           # Project dependencies
│
├── config/                    # Application configurations
│   ├── __init__.py
│   └── config.py             # Configuration classes by environment
│
├── services/                  # Business logic
│   ├── __init__.py
│   └── hello_world_service.py # Hello World service
│
├── blueprints/               # Flask blueprints
│   ├── __init__.py
│   └── hello_world_blueprint.py # Hello World blueprint
│
├── controllers/              # Controllers (maintained for compatibility)
│   ├── __init__.py
│   └── hello_world_controller.py
│
├── utils/                    # Utilities and helpers
│   ├── __init__.py
│   ├── constants.py         # Application constants
│   └── decorators.py        # Useful decorators
│
└── tests/                   # Automated tests
    ├── __init__.py
    ├── test_app.py         # Integration tests
    └── test_hello_world_service.py # Unit tests
```

## 🎯 Applied Principles

### 1. **Object-Oriented Programming**
- **Encapsulation**: Each class has well-defined responsibilities
- **Inheritance**: Use of abstract classes (`BaseService`, `BaseController`, `Config`)
- **Polymorphism**: Different configuration implementations by environment
- **Abstraction**: Clear interfaces between layers

### 2. **Design Patterns**
- **Factory Pattern**: `AppFactory` for application creation
- **Service Layer**: Business logic separation in services
- **Blueprint Pattern**: Modular route organization

### 3. **Python Best Practices**
- **Type Hints**: Static typing in all functions
- **Docstrings**: Complete documentation of classes and methods
- **PEP 8**: Standardized code formatting
- **Separation of concerns**: Each module has a specific function

## 🚀 How to Run

### Installation
```bash
pip install -r requirements.txt
```

### Execution
```bash
# Development (default)
python app.py

# Or specifying the environment
FLASK_ENV=development python app.py
```

### Environment Variables
```bash
FLASK_ENV=development|production|testing
HOST=127.0.0.1
PORT=5000
SECRET_KEY=your-secret-key
DATABASE_URL=your-database-url
```

## 🧪 Testing

### Run all tests
```bash
python -m unittest discover tests/
```

### Run specific tests
```bash
python -m unittest tests.test_hello_world_service
python -m unittest tests.test_app
```

### With pytest (recommended)
```bash
pytest tests/
pytest tests/ --cov=. --cov-report=html
```

## 📡 Endpoints

### GET `/`
Returns default greeting
```json
{
  "message": "Hello, World!"
}
```

### GET `/hello/<name>`
Returns personalized greeting
```json
{
  "message": "Hello, Python!!"
}
```

### POST `/greeting`
Updates the greeting message
```json
{
  "greeting": "New greeting"
}
```

## 🔧 Development Tools

### Code Formatting
```bash
black .
```

### Linting
```bash
flake8 .
```

### Type Checking
```bash
mypy .
```

## 📈 Implemented Improvements

1. **Environment Configuration**: Different configurations for development, production, and testing
2. **Dependency Injection**: Services are injected into controllers
3. **Error Handling**: Global and specific handlers
4. **Data Validation**: Decorators for automatic validation
5. **Logging**: Prepared for structured logging implementation
6. **Testing**: Unit and integration test coverage
7. **Documentation**: Docstrings and type hints throughout the code

## 🎨 Extensibility

The architecture allows easy extension:

1. **New Services**: Extend `BaseService`
2. **New Controllers**: Extend `BaseController`
3. **New Blueprints**: Follow the `HelloWorldBlueprint` pattern
4. **New Configurations**: Implement the abstract `Config` class

## 📝 Next Steps

- [ ] Implement JWT authentication
- [ ] Add database (SQLAlchemy)
- [ ] Implement caching (Redis)
- [ ] Add structured logging
- [ ] Implement API versioning
- [ ] Add Swagger/OpenAPI documentation
