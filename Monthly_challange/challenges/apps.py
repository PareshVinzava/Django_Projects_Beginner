from django.apps import AppConfig


class ChallangesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'challenges'  # We have to write app name here and this app name and app name we register into setting.py should be same otherwise it can create troubles.
