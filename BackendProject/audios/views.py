from django.shortcuts import render
from rest_framework import generics, mixins
from .models import Audio, AudioSegment
from .serializers import (
    AudioSerializer,
    # UpdateAudioSerializer,
    AudioSegmentSerializer,
    AudioUpdateUser,
)
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view


class AudioCreateAPIView(generics.CreateAPIView):
    queryset = Audio.objects.all()
    serializer_class = AudioSerializer


audio_create_view = AudioCreateAPIView.as_view()


class AudioListCreateAPIView(generics.ListCreateAPIView):
    queryset = Audio.objects.all()
    serializer_class = AudioSerializer

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        request = self.request
        if request.user.is_authenticated:
            user = request.user

            if not user.is_superuser:
                return qs.filter(anatator=request.user)
        return qs


audio_list_create_view = AudioListCreateAPIView.as_view()


class AudioSegmentUpdateAPIView(generics.UpdateAPIView):
    queryset = Audio.objects.all()
    serializer_class = AudioUpdateUser
    lookup_field = "id"


audio_update_view = AudioSegmentUpdateAPIView.as_view()


class AudioDestroyAPIView(generics.DestroyAPIView):
    queryset = Audio.objects.all()
    serializer_class = AudioSerializer
    lookup_field = "id"

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


audio_destroy_view = AudioDestroyAPIView.as_view()


#For DetailVue  
class AudiotDetailAPIView(generics.RetrieveAPIView):
    queryset = Audio.objects.all()
    serializer_class = AudioSerializer
    lookup_field = "id"

audio_detail_view = AudiotDetailAPIView.as_view()


@api_view(["GET"])
def login_user(request):
    if request.user.is_authenticated:
        return JsonResponse(
            {
                "id": request.user.id,
                "name": request.user.name,
                "email": request.user.email,
            }
        )
    return JsonResponse({})
