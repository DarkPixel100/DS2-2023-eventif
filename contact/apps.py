from django.apps import AppConfig


class ContactsConfig(AppConfig):
    name = "contact"
    verbose_name = "Mensagens"

    def ready(self):
        import contact.signals