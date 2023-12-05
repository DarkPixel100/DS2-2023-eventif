from django.conf import settings
from django.contrib import messages
from django.core import mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url as r
from django.template.loader import render_to_string

from contact.forms import ContactForm


def contact(request):
    if request.method == "POST":
        return create_contact(request)
    return show_contact_form(request)


def create_contact(request):
    form = ContactForm(request.POST)

    if not form.is_valid():
        return show_contact_form(request, form)

    contact_data = form.save()
    _send_contact_email(
        subject="Contato eventif",
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=(settings.DEFAULT_FROM_EMAIL, contact_data.email),
        template_name="contact/contact_email.txt",
        context={"contact": contact_data},
    )

    messages.success(request, "Contato concluído!")
    return HttpResponseRedirect(r("contact"))


def show_contact_form(request, form=ContactForm()):
    return render(request, "contact/contact_form.html", {"form": form})


def _send_contact_email(subject, from_email, to, template_name, context):
    email_body = render_to_string(template_name, context)
    mail.send_mail(subject, email_body, from_email, to)
