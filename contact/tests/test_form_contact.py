from django.test import TestCase
from contact.forms import ContactForm


class ContactFormTest(TestCase):
    def setUp(self):
        self.form = ContactForm()

    def test_form_has_expected_fields(self):
        expected_fields = ["name", "phone", "email", "message"]
        self.assertListEqual(list(self.form.fields), expected_fields)

    def test_name_is_capitalized(self):
        form = self.make_validated_form(name="DIEGO FONTES DE AVILA")
        self.assertEqual("Diego Fontes De Avila", form.cleaned_data["name"])

    def test_phone_is_optional(self):
        form = self.make_validated_form(phone="")
        self.assertFalse(form.errors)

    def test_empty_phone_is_set_to_default(self):
        form = self.make_validated_form(phone="")
        self.assertEqual(form.cleaned_data["phone"], "Não inserido")

    def make_validated_form(self, **kwargs):
        valid_data = {
            "name": "Diego",
            "email": "diego.avila@aluno.riogrande.ifrs.edu.br",
            "phone": "53-99976-2828",
            "message": "Mensagem teste",
        }
        data = {**valid_data, **kwargs}
        form = ContactForm(data)
        form.is_valid()
        return form