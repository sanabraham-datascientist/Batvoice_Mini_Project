from .models import Audio, AudioSegment
from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

User = get_user_model()


class AudioTestCase(TestCase):
    def setUp(self):
        self.anatator_test = User.objects.create_user("abc", password="abc123")
        self.audio_test = Audio.objects.create(
            title="this is for testing",
            audio_file="uploads\\HealthInsurance.mp3",
            customer="testing customer",
            anatator=self.anatator_test,
        )

    def test_check_character_set(self):
        to_be_checked = "àmili,"
        # to_be_checked "hel@lo" 'm"k' "àmili"
        segment_test = AudioSegment(
            audio=self.audio_test,
            audio_file="media\\uploads\\health_-01.mp3",
            transcript=to_be_checked,
        )
        segment_test.full_clean()

    def test_check_space(self):
        to_be_checked = "sa n a,"
        # to_be_checked = " sana" "sana " " sana " "àmil  i"
        segment_test = AudioSegment(
            audio=self.audio_test,
            audio_file="media\\uploads\\health_-01.mp3",
            transcript=to_be_checked,
        )
        segment_test.full_clean()

    def test_check_capital_letters(self):
        to_be_checked = " sana,"
        # to_be_checked  "SANA " "SAnNA " " sana " "sana"
        segment_test = AudioSegment(
            audio=self.audio_test,
            audio_file="media\\uploads\\health_-01.mp3",
            transcript=to_be_checked,
        )
        segment_test.full_clean()

    def test_check_the_end_text(self):
        to_be_checked = "sana? M"
        # "sana? M" "sana!" "sana:" "sana: "
        segment_test = AudioSegment(
            audio=self.audio_test,
            audio_file="media\\uploads\\health_-01.mp3",
            transcript=to_be_checked,
        )
        segment_test.full_clean()

