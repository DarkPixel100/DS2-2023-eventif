from django.core import mail
from django.test import TestCase


class MailTest(TestCase):
    def setUp(self):
        data = {
            "name": "Diego",
            "phone": "53-99976-2828",
            "email": "diego.avila@aluno.riogrande.ifrs.edu.br",
            "message": "oi",
        }
        self.response = self.client.post("/contato/", data)
        self.email = mail.outbox[0]

    def assert_email_field_equal(self, field_name, expected_value):
        actual_value = getattr(self.email, field_name)
        self.assertEqual(expected_value, actual_value)

    def test_contact_email_subject(self):
        self.assert_email_field_equal("subject", "Contato eventif")

    def test_contact_email_sender(self):
        self.assert_email_field_equal("from_email", "contato@eventif.com.br")

    def test_contact_email_to(self):
        expected_to = [
            "contato@eventif.com.br",
            "diego.avila@aluno.riogrande.ifrs.edu.br",
        ]
        self.assertEqual(expected_to, self.email.to)

    def test_contact_body(self):
        contents = [
            "Diego",
            "53-99976-2828",
            "diego.avila@aluno.riogrande.ifrs.edu.br",
            "oi",
        ]
        email_body = self.email.body
        self.assertTrue(all(content in email_body for content in contents))