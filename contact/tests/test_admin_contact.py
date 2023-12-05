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

        self.model_admin = ContactModelAdmin(Contact, admin.site)