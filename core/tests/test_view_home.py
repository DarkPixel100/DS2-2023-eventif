from django.test import TestCase
from django.shortcuts import resolve_url as r

class TestHome(TestCase):
    def setUp(self):
        self.response = self.client.get(r('home'))
    
    def test_home(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template_used(self):
        self.assertTemplateUsed(self.response,'index.html')

    def test_subscription_link(self):
        expect = 'href="{}"'.format(r('subscriptions:new'))
        self.assertContains(self.response, expect)

    def test_contact_link(self):
        self.assertContains(self.response, 'href="/contato/"')
    
    def test_speakers(self):
        contents = [
            'Grace Hopper',
            'https://cleberfonseca.com.br/img/hopper.jpeg',
            'Alan Turing',
            'https://cleberfonseca.com.br/img/turing.jpeg'
        ]
        for expected in contents:
            with self.subTest():
                self.assertContains(self.response, expected)

    def test_speakers_link(self):
        expected = 'href="{}#speakers"'.format(r('home'))
        self.assertContains(self.response, expected)