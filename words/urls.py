from django.urls import path
from . import views

app_name = 'words'

urlpatterns = [
    path('', views.word_list, name='word_list'),               # List all words
    path('create/', views.word_create, name='word_create'),    # Create a new word
    path('<int:pk>/update/', views.word_update, name='word_update'),  # Update a word
    path('<int:pk>/delete/', views.word_delete, name='word_delete'),  # Delete a word
]
