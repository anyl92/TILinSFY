from django.urls import path
from . import views

app_name = 'movie'

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('create/', views.new_movie, name='new_movie'),
    path('<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('<int:movie_id>/update', views.update_movie, name='update_movie'),
    path('<int:movie_id>/delete', views.delete_movie, name='delete_movie'),
    path('<int:movie_id>/reviews/', views.new_review, name='new_review'),
]
