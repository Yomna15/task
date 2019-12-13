from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('register/', views.register, name='register'),
    path('api/register/',views.RegisterAPIView.as_view()),
]
