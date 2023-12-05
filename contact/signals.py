from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from contact.views import _send_contact_email as send_contact_email
from contact.models import Contact


@receiver(post_save, sender=Contact)
def message_replied(instance, created, update_fields, **kwargs):
    if not created and "response" in update_fields:
        send_contact_email(
            subject="Resposta Contato EventIf",
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=(instance.email, settings.DEFAULT_FROM_EMAIL),
            template_name="contact/contact_response.txt",
            context={"reply": instance},
        )
