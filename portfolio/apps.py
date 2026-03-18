from django.apps import AppConfig


class PortfolioConfig(AppConfig):
    name = 'portfolio'

    def ready(self):
        import portfolio.signals  # noqa: F401 – registers the user_logged_in signal
