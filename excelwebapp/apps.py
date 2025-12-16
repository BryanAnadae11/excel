from django.apps import AppConfig


class ExcelwebappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'excelwebapp'

    def ready(self):
    	import excelwebapp.signals
