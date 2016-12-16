import os

from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TransactionTestCase

from attendee.models import Attendee
from talk.models import Speaker, Talk

User = get_user_model()


class SpeakerTest(TransactionTestCase):
    def setUp(self):
        user = User.objects.create_user(email='test@example.org')
        self.attendee = Attendee.objects.create(user=user)

    def test_str(self):
        speaker = Speaker.objects.create(
            user=self.attendee, videopermission=True, shirt_size=1)
        self.assertEqual("{}".format(speaker), "{}".format(self.attendee))

    def test_create_thumbnail_png(self):
        speaker = Speaker.objects.create(
            user=self.attendee, videopermission=True, shirt_size=1)
        speaker.portrait = SimpleUploadedFile(
            name='mu_at_mil_house.png',
            content=open(os.path.join(os.path.dirname(__file__), 'mu_at_mil_house.png'), 'rb').read(),
            content_type='image/png')
        speaker.create_thumbnail()
        self.assertIsNotNone(speaker.thumbnail.name)

    def test_create_thumbnail_jpg(self):
        speaker = Speaker.objects.create(
            user=self.attendee, videopermission=True, shirt_size=1)
        speaker.portrait = SimpleUploadedFile(
            name='mu_at_mil_house.jpg',
            content=open(os.path.join(os.path.dirname(__file__), 'mu_at_mil_house.jpg'), 'rb').read(),
            content_type='image/jpeg')
        speaker.create_thumbnail()
        self.assertIsNotNone(speaker.thumbnail.name)

    def test_create_thumbnail_other(self):
        speaker = Speaker.objects.create(
            user=self.attendee, videopermission=True, shirt_size=1)
        speaker.portrait = SimpleUploadedFile(
            name='mu_at_mil_house.svg',
            content=open(os.path.join(os.path.dirname(__file__), 'mu_at_mil_house.svg'), 'rb').read(),
            content_type='application/xml+svg')
        speaker.create_thumbnail()
        self.assertIsNone(speaker.thumbnail.name)

    def test_save_creates_thumbnail(self):
        speaker = Speaker.objects.create(
            user=self.attendee, videopermission=True, shirt_size=1)
        speaker.portrait = SimpleUploadedFile(
            name='mu_at_mil_house.jpg',
            content=open(os.path.join(os.path.dirname(__file__), 'mu_at_mil_house.jpg'), 'rb').read(),
            content_type='image/jpeg')
        speaker.save()
        self.assertIsNotNone(speaker.thumbnail.name)


class TalkTest(TransactionTestCase):
    def setUp(self):
        user = User.objects.create_user(email='test@example.org')
        attendee = Attendee.objects.create(user=user)
        self.speaker = Speaker.objects.create(
            user=attendee, videopermission=True, shirt_size=1)

    def test_str(self):
        talk = Talk.objects.create(
            speaker=self.speaker, title='Test', abstract='Test abstract',
            remarks='Test remarks',
        )
        self.assertEqual('{}'.format(talk), '{} - {}'.format(self.speaker, 'Test'))
