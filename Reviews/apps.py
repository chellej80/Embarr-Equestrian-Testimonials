"""
Import app configuration

"""
from django.apps import AppConfig


class ReviewsConfig(AppConfig):
    """Reviews app config"""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Reviews'
