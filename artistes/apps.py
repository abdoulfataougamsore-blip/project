from django.apps import AppConfig


class ArtistesConfig(AppConfig):
    
    name = 'artistes'

    def ready(self):
        import artistes.signals
