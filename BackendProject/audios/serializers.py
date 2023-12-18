from rest_framework import serializers
from .models import Audio,AudioSegment
from rest_framework.reverse import reverse


class UserPublicSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    is_superuser = serializers.BooleanField(read_only=True)

# class AudioSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     audiosegments = serializers.ModelSerializer()
#     def get_audiosegments(self,obj):
#         my_audiosegments = obj.audiosegment_set.all()
#         return my_audiosegments

class AudioInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
            view_name='audio-detail',
            lookup_field='id',
            read_only=True
    )


class AudioSegmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioSegment
        fields = (
            "id",
            "audio_file",
            "length",
            "transcript",
            "audio"
           
        )

    

class AudioSerializer(serializers.ModelSerializer):
    updated_by = UserPublicSerializer(source="anatator", read_only=True)
    segments = AudioSegmentSerializer(many=True)
    length = serializers.IntegerField(read_only=True)
    status = serializers.CharField(read_only=True)
    created_at = serializers.DateField(read_only=True)
    updated_at = serializers.DateField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name="audio-detail", lookup_field="id"
    )

    class Meta:
        model = Audio
        fields = [
            "id",
            "segments",
            "title",
            "length",
            "audio_file",
            "customer",
            "status",
            "anatator",
            "created_at",
            "updated_at",
            "description",
            "url",
            "edit_url",
            "updated_by",
        ]

    def get_my_user_data(self, obj):
        return {
            "username": obj.anatator.username,
            "is_super_user": obj.anatator.is_superuser,
       }
    
    def get_edit_url(self, obj):
        request = self.context.get("request")  # self.request
        if request is None:
            return None
        return reverse("audio-edit", kwargs={"id": obj.id}, request=request)



class AudioSegmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioSegment
        fields = (
            "id",
            "audio_file",
            "length",
            "transcript",
            "audio"
           
        )

class UpdateAudioSerializer(serializers.ModelSerializer):
    segments = AudioSegmentSerializer(many=True)

    class Meta:
        model = Audio
        fields = ['id', 'segments']

    def create(self, validated_data):
        tracks_data = validated_data.pop('tracks')
        audio = Audio.objects.create(**validated_data)
        for track_data in tracks_data:
            AudioSegment.objects.create(audio=audio, **track_data)
        return audio