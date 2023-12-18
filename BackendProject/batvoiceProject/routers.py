from rest_framework.routers import DefaultRouter
from audios.viewsets import AudioViewSet

router = DefaultRouter()
router.register('audios',AudioViewSet,basename='products')

urlpatterns = router.urls