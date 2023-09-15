from django.core import mail
from django.test import TestCase

class MailTest(TestCase):
    def setUp(self):
        data = {
            "name": "Diego",
            "phone": "53-99101-1002",
            "email": "diego.avila@aluno.riogrande.ifrs.edu.br",
            "message": "oi",
        }
        self.response = self.client.post('/contato/', data)
        self.email = mail.outbox[0]

    def assertEmailFieldEqual(self, field_name, expected_value):
        actual_value = getattr(self.email, field_name)
        self.assertEqual(expected_value, actual_value)

    def test_contact_email_subject(self):
        self.assertEmailFieldEqual("subject", "Contato eventif")

    def test_contact_email_sender(self):
        self.assertEmailFieldEqual("from_email", "contato@eventif.com.br")

    def test_contact_email_to(self):
        expected_to = ['contato@eventif.com.br', 'diego.avila@aluno.riogrande.ifrs.edu.br']
        self.assertEqual(expected_to, self.email.to)

    def test_contact_body(self):
        contents = ["Diego", "53-99101-1002", "diego.avila@aluno.riogrande.ifrs.edu.br", "oi"]
        email_body = self.email.body
        self.assertTrue(all(content in email_body for content in contents))