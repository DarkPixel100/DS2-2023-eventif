from django.test import TestCase
from django.core import mail
from django.shortcuts import resolve_url as r

from contact.forms import ContactForm


class ContactGetTest(TestCase):
    def setUp(self):
        self.response = self.client.get(r("contact"))

    def test_contact_form_get_status_code(self):
        self.assertEqual(200, self.response.status_code)

    def test_contact_form_get_template_used(self):
        self.assertTemplateUsed(self.response, "contact/contact_form.html")

    def test_contact_form_structure(self):
        tags = [
            ("<form", 1),
            ("<input", 5),
            ('type="text"', 2),
            ("<textarea", 1),
            ('type="email"', 1),
            ('type="submit"', 1),
        ]
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.response, text, count)

    def test_contact_form_has_valid_form_instance(self):
        form = self.response.context["form"]
        self.assertIsInstance(form, ContactForm)


class ContactPostValidTest(TestCase):
    def test_submit_valid_contact_form(self):
        data = {
            "name": "Diego",
            "phone": "53-99976-2828",
            "email": "diego.avila@aluno.riogrande.ifrs.edu.br",
            "message": "Mensagem teste.",
        }
        response = self.client.post(r("contact"), data)
        self.assertEqual(302, response.status_code)
        self.assertEqual(1, len(mail.outbox))


class ContactPostInvalidTest(TestCase):
    def test_submit_invalid_contact_form(self):
        response = self.client.post(r("contact"), {})
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, "contact/contact_form.html")
        form = response.context["form"]
        self.assertIsInstance(form, ContactForm)
        self.assertTrue(form.errors)


class ContactSuccessMessageTest(TestCase):
    def test_submit_contact_form_with_success_message(self):
        data = {
            "name": "Diego",
            "phone": "53-99976-2828",
            "email": "diego.avila@aluno.riogrande.ifrs.edu.br",
            "message": "Mensagem teste.",
        }
        response = self.client.post(r("contact"), data, follow=True)

        self.assertContains(response, "Contato concluído!")
