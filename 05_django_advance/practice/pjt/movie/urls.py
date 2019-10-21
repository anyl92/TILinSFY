from django.urls import path
from . import views

app_name = 'movie'

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('create/', views.new_movie, name='new_movie'),
    path('<int:movie_id>/', views.movie_detail, name='movie_detail'),
    
]
