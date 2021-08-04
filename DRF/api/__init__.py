from django.apps import AppConfig

class ApiConfig(AppConfig):
    name = 'full.python.path.to.your.app.api'
    label = 'my.api'
default_app_config = 'full.python.path.to.your.app.api.apps.ApiConfig'