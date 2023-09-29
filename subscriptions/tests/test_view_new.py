from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r

from subscriptions.forms import SubscriptionForm
from subscriptions.models import Subscription

class SubscriptionsNewGet(TestCase):
    def setUp(self):
        self.response = self.client.get(r('subscriptions:new'))

    def test_get(self):
        """GET /inscricao/ must return status_code 200"""
        response = self.client.get('/inscricao/')
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use subscriptions/subscription_fotm.html"""
        self.assertTemplateUsed(
            self.response, 'subscriptions/subscription_form.html')

    def test_html(self):
        """HTML must contain 5 input tags"""
        tags = (('<form', 1),
                ('<input', 6),
                ('type="text"', 3),
                ('type="email"', 1),
                ('type="submit"', 1))
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.response, text, count)

    def test_csrf(self):
        """HTML must contain CSRF"""
        self.assertContains(self.response, "csrfmiddlewaretoken")

    def test_has_form(self):
        """Context must have subscription form"""
        form = self.response.context["form"]
        self.assertIsInstance(form, SubscriptionForm)

class SubscriptionsNewPostValid(TestCase):
    def setUp(self):
        data = dict(name="Diego",
                    cpf="12345678901",
                    email="diego.avila@aluno.riogrande.ifrs.edu.br",
                    phone="53-99101-1002")
        self.response = self.client.post(r('subscriptions:new'), data)

    def test_post(self):
        self.assertRedirects(self.response,  r('subscriptions:detail', 1))

    def test_send_subscribe_email(self):
        self.assertEqual(1, len(mail.outbox))
        
    def test_save_subscription(self):
        self.assertTrue(Subscription.objects.exists())


class SubscriptionsNewPostInvalid(TestCase):
    def setUp(self):
        self.response = self.client.post(r('subscriptions:new'), {})

    def test_post(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(
            self.response, 'subscriptions/subscription_form.html')

    def test_has_form(self):
        form = self.response.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_error(self):
        form = self.response.context['form']
        self.assertTrue(form.errors)
    
    def test_dont_save_subsctiption(self):
        self.assertFalse(Subscription.objects.exists())