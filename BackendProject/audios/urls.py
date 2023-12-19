from django.urls import path



from . import views 

namespace='audios'

urlpatterns = [
    path('', views.audio_list_create_view, name='audio-list'),
    path('<int:id>/update/', views.audio_update_view, name='audio-edit'),
    path('<int:id>/delete/', views.audio_destroy_view),
    path('<int:id>/', views.audio_detail_view, name='audio-detail'),
    path('admin/add', views.audio_create_view, name='audio-create')
   
]

