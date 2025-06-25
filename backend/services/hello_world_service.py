"""
Application services.
"""
from abc import ABC, abstractmethod
from typing import Dict, Any


class BaseService(ABC):
    """Abstract base class for services."""
    
    @abstractmethod
    def process(self, data: Any) -> Any:
        """Processes data according to business rules."""
        pass


class HelloWorldService(BaseService):
    """Service for Hello World business logic."""
    
    def __init__(self, greeting: str = "Hello, World!"):
        """
        Initializes the service.
        
        Args:
            greeting: Custom greeting message
        """
        self._greeting = greeting
    
    def process(self, data: Dict[str, Any] = None) -> Dict[str, str]:
        """
        Processes the greeting request.
        
        Args:
            data: Optional data for customization
            
        Returns:
            Dictionary with the greeting message
        """
        if data and 'name' in data:
            message = f"{self._greeting.replace('World', data['name'])}!"
        else:
            message = self._greeting
        
        return {"message": message}
    
    def set_greeting(self, greeting: str) -> None:
        """
        Sets a new greeting message.
        
        Args:
            greeting: New greeting message
        """
        self._greeting = greeting
    
    def get_greeting(self) -> str:
        """
        Returns the current greeting message.
        
        Returns:
            Greeting message
        """
        return self._greeting
