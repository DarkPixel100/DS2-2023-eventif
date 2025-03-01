from django.test import TestCase
from django.shortcuts import resolve_url as r
from core.models import Speaker


class SpeakerModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name="Grace Hopper",
            slug="grace-hopper",
            website="https://pt.wikipedia.org/wiki/Grace_Hopper",
            photo="https://cleberfonseca.com.br/img/hopper.jpeg",
            description="Programadora e almirante.",
        )

    def test_create(self):
        self.assertTrue(Speaker.objects.exists())

    def test_description_can_be_blank(self):
        field = Speaker._meta.get_field("description")
        self.assertTrue(field.blank)

    def test_website_can_be_blank(self):
        field = Speaker._meta.get_field("website")
        self.assertTrue(field.blank)

    def test_str(self):
        self.assertEqual("Grace Hopper", str(self.speaker))

    def test_get_absolute_url(self):
        url = r("speaker_detail", slug=self.speaker.slug)
        self.assertEqual(url, self.speaker.get_absolute_url())
