from django.shortcuts import render
from rest_framework import generics, mixins
from .models import Audio, AudioSegment
from .serializers import AudioSerializer,UpdateAudioSerializer,AudioSegmentSerializer


class AudioListCreateAPIView(generics.ListCreateAPIView):
    queryset = Audio.objects.all()
    serializer_class = AudioSerializer

        
    # def get_queryset(self, *args, **kwargs):
    #     qs = super().get_queryset(*args, **kwargs)
    #     request = self.request
    #     user = request.user

    #     if not user.is_superuser:
    #         return qs.filter(anatator=request.user)
    #     return qs

audio_list_create_view = AudioListCreateAPIView.as_view()


class AudioUpdateAPIView(generics.UpdateAPIView):
    queryset = AudioSegment.objects.all()
    serializer_class = AudioSegmentSerializer
    lookup_field = "id"

    # def perform_update(self, serializer):
    #     instance = serializer.save()
    #     if not instance.description:
    #         instance.content = instance.title


audio_update_view = AudioUpdateAPIView.as_view()


class AudioDestroyAPIView(generics.DestroyAPIView):
    queryset = Audio.objects.all()
    serializer_class = AudioSerializer
    lookup_field = "id"

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


audio_destroy_view = AudioDestroyAPIView.as_view()


class AudiotDetailAPIView( generics.RetrieveAPIView):
    queryset = Audio.objects.all()
    serializer_class = AudioSerializer
    lookup_field = 'id' 

audio_detail_view = AudiotDetailAPIView.as_view()
