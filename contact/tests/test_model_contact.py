from django.test import TestCase
from contact.models import Contact
from datetime import datetime


class ContactModelTest(TestCase):
    def setUp(self):
        self.contact = Contact.objects.create(
            name="Diego Avila",
            email="diego.avila@aluno.riogrande.ifrs.edu.br",
            phone="53-99976-2828",
            message="Mensagem teste",
        )

    def test_contact_created(self):
        self.assertTrue(Contact.objects.exists())

    def test_phone_can_be_blank(self):
        field = Contact._meta.get_field("phone")
        self.assertTrue(field.blank)

    def test_created_at(self):
        self.assertIsInstance(self.contact.created_at, datetime)

    def test_replied_default_false(self):
        self.assertFalse(self.contact.replied)

    def test_contact_str(self):
        self.assertEqual("Diego Avila", str(self.contact))
