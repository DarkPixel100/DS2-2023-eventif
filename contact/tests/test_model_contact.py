from django.test import TestCase
from contact.models import Contact


class ContactModelTest(TestCase):
    def setUp(self):
        self.contact = Contact.objects.create(
            name="Diego Avila",
            email="diego.avila@aluno.riogrande.ifrs.edu.br",
            phone="53-99976-2828",
            message="Mensagem teste",
        )

    def test_create(self):
        self.assertTrue(Contact.objects.exists())

    def test_phone_can_be_blank(self):
        field = Contact._meta.get_field("phone")
        self.assertTrue(field.blank)

    def test_message_can_be_blank(self):
        field = Contact._meta.get_field("message")
        self.assertTrue(field.blank)

    def test_str(self):
        self.assertEqual("Diego Avila", str(self.contact))
