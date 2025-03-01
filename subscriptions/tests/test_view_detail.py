from django.test import TestCase
from django.shortcuts import resolve_url as r

from subscriptions.models import Subscription


class SubscriptionDetailGet(TestCase):
    def setUp(self):
        self.obj = Subscription.objects.create(
            name="Diego",
            cpf="12345678901",
            email="diego.avila@aluno.riogrande.ifrs.edu.br",
            phone="53-99976-2828",
        )
        self.resp = self.client.get(r("subscriptions:detail", self.obj.pk))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, "subscriptions/subscription_detail.html")

    def test_context(self):
        sub = self.resp.context["subscription"]
        self.assertIsInstance(sub, Subscription)

    def test_html(self):
        contents = (self.obj.name, self.obj.cpf, self.obj.email, self.obj.phone)
        for content in contents:
            with self.subTest():
                self.assertContains(self.resp, content)


class SubscriptionDetailNotFount(TestCase):
    def test_not_found(self):
        resp = self.client.get(r("subscriptions:detail", 0))
        self.assertEqual(404, resp.status_code)
