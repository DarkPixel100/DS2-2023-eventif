from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r


class MailTest(TestCase):
    def setUp(self):
        data = dict(
            name="Diego",
            cpf="12345678901",
            email="diego.avila@aluno.riogrande.ifrs.edu.br",
            phone="53-99976-2828",
        )
        self.response = self.client.post(r("subscriptions:new"), data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = "Confirmação de inscrição"
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_sender(self):
        expect = "contato@eventif.com.br"
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ["contato@eventif.com.br", "diego.avila@aluno.riogrande.ifrs.edu.br"]
        self.assertEqual(expect, self.email.to)

    def test_subscription_body(self):
        contents = [
            "Diego",
            "12345678901",
            "diego.avila@aluno.riogrande.ifrs.edu.br",
            "53-99976-2828",
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
