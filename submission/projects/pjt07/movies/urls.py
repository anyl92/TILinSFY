from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('<int:movie_id>/reviews/new/', views.review_create, name='review_create'),
    path('<int:movie_id>/reviews/<int:review_id>/delete/', views.review_delete, name='review_delete'),
    path('<int:movie_id>/like', views.like_save, name='like_save'),
]
