from django.apps import AppConfig


class MoviesiteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'moviesite'

    def ready(self):
        import moviesite.signals
