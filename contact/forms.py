from django import forms
from contact.models import Contact
from django.core.exceptions import ValidationError


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "phone", "email", "message"]

    def clean_name(self):
        name = self.cleaned_data["name"]
        words = [word.capitalize() for word in name.split()]
        return " ".join(words)

    def clean_phone(self):
        phone = self.cleaned_data["phone"]
        return "Não inserido" if phone == "" else phone
