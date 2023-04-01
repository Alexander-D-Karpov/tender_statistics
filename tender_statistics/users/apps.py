from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "tender_statistics.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import tender_statistics.users.signals  # noqa F401
        except ImportError:
            pass
