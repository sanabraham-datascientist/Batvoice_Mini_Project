from rest_framework import mixins, viewsets

from .models import Audio
from .serializers import AudioSerializer

class AudioViewSet(viewsets.ModelViewSet):
    '''
    get -> list -> queryset
    get -> retrieve instance (Detail View)
    post -> create -> new instance
    put -> update
    patch -> partial update
    delete -> destroy 
    
    '''
    queryset = Audio.objects.all()
    serializer_class = AudioSerializer
    lookup_field = 'pk' 