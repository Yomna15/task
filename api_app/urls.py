from django.urls import path
from . import views

urlpatterns = [
    path('distance/', views.get_distance, name='get_distance')
]
