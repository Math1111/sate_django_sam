#mymovies/movies/urls.py
from django.urls import path
from .views import movie_list
from . import views
from .views import SignUpView

urlpatterns = [
    path('', views.movie_list, name='movie_list'),  # Список фильмов
    path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),
]
