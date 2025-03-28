from django.urls import path
from .views import movie_list
from . import views

urlpatterns = [
    #path('', movie_list, name='movie_list'),#если что убрать то то
    path('', views.movie_list, name='movie_list'),  # Список фильмов
    path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),
]
# возможно в другой Urls надо добавлять