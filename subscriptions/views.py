from django.conf import settings
from django.contrib import messages
from django.core import mail
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, resolve_url as r
from django.template.loader import render_to_string

from subscriptions.forms import SubscriptionForm
from subscriptions.models import Subscription


def new(request):
    if request.method == "POST":
        return create(request)

    return empty_form(request)


def empty_form(request):
    return render(
        request, "subscriptions/subscription_form.html", {"form": SubscriptionForm()}
    )


def create(request):
    form = SubscriptionForm(request.POST)

    if not form.is_valid():
        return render(request, "subscriptions/subscription_form.html", {"form": form})

    sub = form.save()

    _send_mail(
        "Confirmação de inscrição",
        settings.DEFAULT_FROM_EMAIL,
        form.cleaned_data["email"],
        "subscriptions/subscription_email.txt",
        {"subscription": sub},
    )

    return HttpResponseRedirect(r("subscriptions:detail", sub.pk))


def detail(request, pk):
    try:
        sub = Subscription.objects.get(pk=pk)
    except Subscription.DoesNotExist:
        raise Http404
    return render(
        request, "subscriptions/subscription_detail.html", {"subscription": sub}
    )


def _send_mail(subject, from_, to, template_name, context):
    body = render_to_string(template_name, context)
    mail.send_mail(subject, body, from_, [from_, to])
