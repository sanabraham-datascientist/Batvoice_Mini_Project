
from rest_framework import serializers
from .models import Audio,AudioSegment
from rest_framework.reverse import reverse


class AudioSegmentUpdateUser(serializers.ModelSerializer):

    id = serializers.IntegerField()
    class Meta:
        model = AudioSegment
        fields = ("id", "transcript")


class AudioUpdateUser(serializers.ModelSerializer):

    id = serializers.IntegerField()
    segments = AudioSegmentUpdateUser(many=True)

    class Meta:
        model = Audio
        fields = ['id', 'segments']


    def create(self, validated_data):
        segments_validated_data = validated_data.pop('segments')
        audio_instance = Audio.objects.create(**validated_data)
        for segment in segments_validated_data:
            AudioSegment.objects.create(audio=audio_instance,**segment)
        return audio_instance

    # update() method does not support writable nested fields by default
    def update(self, instance, validated_data):
        segments_id_instances_list=[]
        segments_validated_data = validated_data.pop('segments')
        for segment_validated_data in segments_validated_data:
            if "id" in segment_validated_data.keys():
                if AudioSegment.objects.filter(id=segment_validated_data['id']).exists():
                    segment_instance = AudioSegment.objects.get(id=segment_validated_data['id'])
                    segment_instance.transcript= segment_validated_data.get('transcript', segment_validated_data['transcript'])
                    segment_instance.save()
                    segments_id_instances_list.append(segment_instance.id)
                else: continue
            else:
                segment_instance = AudioSegment.objects.create(audio=instance, **segment_validated_data)
                segments_id_instances_list.append(segment_instance.id)

  

        return instance

class UserPublicSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    is_superuser = serializers.BooleanField(read_only=True)


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
            "transcript",
        
           
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
            "transcript",
           
        )

