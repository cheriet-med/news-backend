
from datetime import timedelta
from unittest.mock import patch

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from rest_framework.test import APIClient

from .models import Offer, ScheduledEmail


class TriggerEmailsTests(TestCase):
    def test_trigger_emails_sends_each_scheduled_email_only_once(self):
        client = ScheduledEmail.objects.create(
            email='user@example.com',
            name='Test User',
            language='en',
            created_at=timezone.now() - timedelta(days=2),
        )

        with patch('padlevap.utils.send_email1') as send_email1_mock:
            response = self.client.post(
                reverse('trigger_emails'),
                HTTP_X_API_KEY='h!6u@q1w%z$9&l^e*0x+3v#b8s$k@r!m2n(c)p=f$g@u^d&wz',
            )
            self.assertEqual(response.status_code, 200)
            self.assertEqual(send_email1_mock.call_count, 1)

            response = self.client.post(
                reverse('trigger_emails'),
                HTTP_X_API_KEY='h!6u@q1w%z$9&l^e*0x+3v#b8s$k@r!m2n(c)p=f$g@u^d&wz',
            )
            self.assertEqual(response.status_code, 200)
            self.assertEqual(send_email1_mock.call_count, 1)

        client.refresh_from_db()
        self.assertTrue(client.welcome_sent)
        self.assertFalse(client.is_completed)


class OfferEmailSendingTests(TestCase):
    def test_offer_submission_sends_only_one_immediate_email(self):
        user = get_user_model().objects.create_user(email='tester@example.com', password='secret123')
        api_client = APIClient()
        api_client.force_authenticate(user=user)

        payload = {
            'name': 'Test User',
            'email': 'user@example.com',
            'language': 'en',
            'date': '2026-08-08',
            'time': '10:00',
        }

        with patch('padlevap.views.send_mail') as send_mail_mock, \
             patch('padlevap.views.send_third_email.apply_async') as third_mock, \
             patch('padlevap.views.send_fourth_email.apply_async') as fourth_mock, \
             patch('padlevap.views.send_fifth_email.apply_async') as fifth_mock, \
             patch('padlevap.views.send_sixth_email.apply_async') as sixth_mock:
            response = api_client.post(reverse('offer get and post'), payload, format='json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(send_mail_mock.call_count, 1)
        self.assertEqual(Offer.objects.count(), 1)
        third_mock.assert_called_once()
        fourth_mock.assert_called_once()
        fifth_mock.assert_called_once()
        sixth_mock.assert_called_once()

