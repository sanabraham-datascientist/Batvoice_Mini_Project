from django.db import models
from django.utils.timesince import timesince
import uuid
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save, post_save
from django.core.exceptions import ValidationError
from django.conf import settings
import datetime, mutagen
from django.urls import reverse
from .validators import (
    check_character_set,
    check_space,
    check_capital_letters,
    check_the_end_text,
)

User = get_user_model()


class Audio(models.Model):
    
    title = models.CharField(null=False, max_length=50)
    length = models.IntegerField(blank=True, null=True)
    audio_file = models.FileField(upload_to="uploads/", null=False)
    customer = models.CharField(null=False, max_length=30)
    status = models.CharField(default="new", max_length=20)
    anatator = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(blank=True,null=True)
    description = models.TextField(null=True, blank=True)


    @property
    def user_name(self):
        return User.objects.get(id=self.anatator.id).username

    @property
    def updated_at_formatted(self):
        return timesince(self.updated_at)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("audio:detail", kwargs={"id": self.id})

    def get_edit_url(self):
        return reverse("audios:update", kwargs={"id": self.id})

    def get_audio_segment_children(self):
        return self.audiosegment_set.all()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


def audio_pre_save(sender, instance, *args, **kwargs):
    if instance.length is None:
        instance.length = mutagen.File(instance.audio_file).info.length


pre_save.connect(audio_pre_save, sender=Audio)


class AudioSegment(models.Model):
    # uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    audio = models.ForeignKey(Audio,related_name='segments', on_delete=models.CASCADE)
    audio_file = models.FileField(upload_to="uploads/", null=False)
    length = models.IntegerField(blank=True, null=True)
    transcript = models.TextField(
        null=True,
        blank=True,
        default=" ",
        validators=[
            check_character_set,
            check_space,
             check_capital_letters,
             check_the_end_text,
         ],
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


def audio_segment_pre_save(sender, instance, *args, **kwargs):
    if instance.length is None:
        instance.length = mutagen.File(instance.audio_file).info.length
    if instance.length < 8 or instance.length > 20:
        raise ValidationError("The segment length has to be between 8 and 20 ")


pre_save.connect(audio_segment_pre_save, sender=AudioSegment)

