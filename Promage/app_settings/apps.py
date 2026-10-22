from django.apps import AppConfig


class AppSettingsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "app_settings"
    # Keep historical migration app label
    label = "settings"
