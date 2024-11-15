from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('set_language/', views.set_language, name='set_language'),
    path('play/', views.landing, name='play_game'),  # This defines the 'play_game' URL
    path('instructions/', views.landing, name='instructions'),  # This defines the 'instructions' URL
    path('high_scores/', views.landing, name='high_scores'),  # This defines the 'high_scores' URL


]
