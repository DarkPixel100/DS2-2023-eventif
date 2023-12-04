from datetime import datetime
from django.test import TestCase
from subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name="Diego Avila",
            cpf="12345678901",
            email="diegofavila20@gmail.com",
            phone="53999762828",
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual("Diego Avila", str(self.obj))

    def test_paid_defaut_false(self):
        self.assertEqual(False, self.obj.paid)
