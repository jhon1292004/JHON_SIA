from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_anime, name='movie_anime'),
    path('movie/<int:pk>/edit/', views.edit_movie, name='edit_movie'),
    path('movie/<int:pk>/delete/', views.delete_movie, name='delete_movie'),
]