from unittest.mock import Mock
from django.test import TestCase
from contact.admin import ContactModelAdmin, Contact, admin


class ContactModelAdminTest(TestCase):
    def setUp(self):
        Contact.objects.create(
            name="Diego Avila",
            email="diego.avila@aluno.riogrande.ifrs.edu.br",
            phone="53-99976-2828",
            message="Mensagem teste",
        )

        self.contact_model_admin = ContactModelAdmin(Contact, admin.site)

    def test_has_mark_as_replied_action(self):
        self.assertIn("mark_as_replied", self.contact_model_admin.actions)

    def test_action_updates_replied_flag(self):
        # Arrange
        queryset = Contact.objects.all()

        # Act
        self.call_mark_as_replied_action(queryset)

        # Assert
        self.assertEqual(Contact.objects.filter(replied=True).count(), 1)

    def test_action_sends_correct_message(self):
        # Arrange
        queryset = Contact.objects.all()

        # Act
        self.call_mark_as_replied_action(queryset)

        # Assert
        expected_message = "1 mensagem foi respondida."
        self.mock.assert_called_once_with(None, expected_message)

    def call_mark_as_replied_action(self, queryset):
        # Arrange
        self.mock = Mock()
        old_message_user = ContactModelAdmin.message_user
        ContactModelAdmin.message_user = self.mock

        # Act
        self.contact_model_admin.mark_as_replied(None, queryset)

        # Clean up
        ContactModelAdmin.message_user = old_message_user
