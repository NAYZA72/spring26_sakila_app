# Authors: Muhammad Afzaal Akhtar
# Date: 2026-04-25
# Description: Integrated configuration with merged settings from feature branches.

import os

class Config:
    """Base configuration class for the Sakila Flask application."""
    
    # Database connection settings
    # Task A2 Requirement: Keep 'sakila-db-server' as the host [cite: 80]
    MYSQL_HOST = os.environ.get('MYSQL_HOST', 'sakila-db-server')
    MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', 'admin')
    MYSQL_DB = os.environ.get('MYSQL_DB', 'sakila')

    # Merged settings from feature/update-config and feature/add-healthcheck [cite: 80]
    CONNECTION_TIMEOUT = int(os.environ.get('CONNECTION_TIMEOUT', '30'))
    HEALTH_CHECK_INTERVAL = int(os.environ.get('HEALTH_CHECK_INTERVAL', '10'))

    # Security configuration
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key-here-change-this-in-production')