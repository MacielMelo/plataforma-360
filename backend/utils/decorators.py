"""
General application utilities.
"""
import functools
import time
from typing import Any, Callable, Dict
from flask import jsonify


def measure_time(func: Callable) -> Callable:
    """
    Decorator to measure function execution time.
    
    Args:
        func: Function to be decorated
        
    Returns:
        Decorated function with time measurement
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} executed in {end_time - start_time:.4f} seconds")
        return result
    return wrapper


def validate_json_data(required_fields: list) -> Callable:
    """
    Decorator to validate JSON request data.
    
    Args:
        required_fields: List of required fields
        
    Returns:
        Validation decorator
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            from flask import request
            
            data = request.get_json()
            if not data:
                return jsonify({"error": "JSON data is required"}), 400
            
            missing_fields = [field for field in required_fields if field not in data]
            if missing_fields:
                return jsonify({
                    "error": f"Missing required fields: {', '.join(missing_fields)}"
                }), 400
            
            return func(*args, **kwargs)
        return wrapper
    return decorator


def format_response(data: Any, status_code: int = 200) -> tuple:
    """
    Formats a standard API response.
    
    Args:
        data: Data to be returned
        status_code: HTTP status code
        
    Returns:
        Tuple with JSON response and status code
    """
    return jsonify(data), status_code


def handle_service_error(func: Callable) -> Callable:
    """
    Decorator to handle service errors.
    
    Args:
        func: Function to be decorated
        
    Returns:
        Decorated function with error handling
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return jsonify({"error": f"Validation error: {str(e)}"}), 400
        except Exception as e:
            return jsonify({"error": f"Internal error: {str(e)}"}), 500
    return wrapper
