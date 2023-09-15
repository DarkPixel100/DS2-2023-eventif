from django.test import TestCase
from contact.forms import ContactForm

class ContactFormTest(TestCase):
    def setUp(self):
        self.form = ContactForm()

    def test_form_has_fields(self):
        expected_fields = ['name', 'phone', 'email', 'message']
        self.assertListEqual(list(self.form.fields), expected_fields)