"""
Application configuration settings.
"""
import os
from abc import ABC, abstractmethod
from typing import Dict, Any


class Config(ABC):
    """Abstract base class for configurations."""
    
    SECRET_KEY: str = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
    
    @property
    @abstractmethod
    def database_uri(self) -> str:
        """Database URI."""
        pass
    
    @classmethod
    def get_config(cls) -> Dict[str, Any]:
        """Returns a dictionary with the configurations."""
        return {
            'SECRET_KEY': cls.SECRET_KEY,
        }


class DevelopmentConfig(Config):
    """Configuration for development environment."""
    
    DEBUG: bool = True
    TESTING: bool = False
    
    @property
    def database_uri(self) -> str:
        return os.environ.get('DEV_DATABASE_URL', 'sqlite:///dev.db')
    
    @classmethod
    def get_config(cls) -> Dict[str, Any]:
        config = super().get_config()
        config.update({
            'DEBUG': cls.DEBUG,
            'TESTING': cls.TESTING,
        })
        return config


class ProductionConfig(Config):
    """Configuration for production environment."""
    
    DEBUG: bool = False
    TESTING: bool = False
    
    @property
    def database_uri(self) -> str:
        db_url = os.environ.get('DATABASE_URL')
        if not db_url:
            raise ValueError("DATABASE_URL must be defined in production")
        return db_url
    
    @classmethod
    def get_config(cls) -> Dict[str, Any]:
        config = super().get_config()
        config.update({
            'DEBUG': cls.DEBUG,
            'TESTING': cls.TESTING,
        })
        return config


class TestingConfig(Config):
    """Configuration for testing environment."""
    
    DEBUG: bool = True
    TESTING: bool = True
    
    @property
    def database_uri(self) -> str:
        return 'sqlite:///:memory:'
    
    @classmethod
    def get_config(cls) -> Dict[str, Any]:
        config = super().get_config()
        config.update({
            'DEBUG': cls.DEBUG,
            'TESTING': cls.TESTING,
        })
        return config


# Dictionary of available configurations
config_by_name = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}


def get_config(environment: str = 'default') -> Config:
    """
    Returns the configuration based on the environment.
    
    Args:
        environment: Environment name (development, production, testing)
        
    Returns:
        Instance of the appropriate configuration
    """
    config_class = config_by_name.get(environment, DevelopmentConfig)
    return config_class()
