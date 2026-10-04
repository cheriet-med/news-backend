
from datetime import timedelta
from unittest.mock import patch

from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import resolve, reverse
from django.utils import timezone
from rest_framework.test import APIClient

from .models import Offer, Post, ScheduledEmail


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


class OfferRouteTests(TestCase):
    def test_offerid_route_matches_trailing_slash(self):
        match = resolve('/offerid/1/')
        self.assertEqual(match.func.__name__, 'Offerid')
        self.assertEqual(match.kwargs['pk'], 1)


class UserDetailsEndpointTests(TestCase):
    def test_user_details_requires_authentication(self):
        response = self.client.get('/api/user/')
        self.assertEqual(response.status_code, 401)

    def test_user_details_returns_profile_for_authenticated_user(self):
        user = get_user_model().objects.create_user(
            email='profile@example.com',
            password='secret123',
            full_name='Profile User',
        )
        client = APIClient()
        client.force_authenticate(user=user)
        response = client.get('/api/user/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['email'], 'profile@example.com')
        self.assertEqual(response.json()['full_name'], 'Profile User')


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


class PostImageConversionTests(TestCase):
    def test_post_save_handles_localized_image_fields(self):
        image = SimpleUploadedFile('sample.jpg', b'fake-image-content', content_type='image/jpeg')

        with patch('padlevap.models.convert_to_avif') as convert_mock:
            convert_mock.return_value = SimpleUploadedFile(
                'sample.avif',
                b'converted-image-content',
                content_type='image/avif',
            )
            post = Post.objects.create(
                title_en='Example Post',
                image_en=image,
            )

        self.assertTrue(post.image_en.name.lower().endswith('.avif'))
        convert_mock.assert_called_once()

