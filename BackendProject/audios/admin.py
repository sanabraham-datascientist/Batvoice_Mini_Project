from django.contrib import admin
from .models import Audio, AudioSegment
from django.contrib.auth import get_user_model

anatator = get_user_model()


class AudioSegmentInline(admin.StackedInline):
    model = AudioSegment
    readonly_fields = ["length"]
    extra = 0


class AudioAdmin(admin.ModelAdmin):
    inlines = [AudioSegmentInline]
    list_display = ["title"]
    readonly_fields = ["created_at", "length", "status"]
    raw_id_fields = ["anatator"]


admin.site.register(Audio, AudioAdmin)
