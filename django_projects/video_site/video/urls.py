from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('video/<int:video_id>/', views.video, name='video'),
]
