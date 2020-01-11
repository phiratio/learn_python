from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.GetUsersCount.as_view(), name='users_count'),
]
