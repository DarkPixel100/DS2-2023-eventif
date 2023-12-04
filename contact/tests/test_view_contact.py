from django.core import mail
from django.test import TestCase

from contact.forms import ContactForm


class ContactGetTest(TestCase):
    def setUp(self):
        self.response = self.client.get("/contato/")

    def test_get_contact_form_status_code(self):
        self.assertEqual(200, self.response.status_code)

    def test_get_contact_form_template_used(self):
        self.assertTemplateUsed(self.response, "contact/contact_form.html")

    def test_contact_form_structure(self):
        tags = (
            ("<form", 1),
            ("<input", 5),
            ('type="text"', 2),
            ("<textarea", 1),
            ('type="email"', 1),
            ('type="submit"', 1),
        )
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
            "message": "oi",
        }
        response = self.client.post("/contato/", data)
        self.assertEqual(302, response.status_code)
        self.assertEqual(1, len(mail.outbox))


class ContactPostInvalidTest(TestCase):
    def test_submit_invalid_contact_form(self):
        response = self.client.post("/contato/", {})
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
            "message": "oi",
        }
        response = self.client.post("/contato/", data, follow=True)

        self.assertContains(response, "Contato concluído!")
