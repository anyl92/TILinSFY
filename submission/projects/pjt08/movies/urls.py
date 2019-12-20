from django.urls import path
from . import views

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title='Movie API',
        default_version='v1',
        description='영화제공 API입니다',
    )
)

app_name = 'movies'

urlpatterns = [
    path('genres/', views.genre_list, name='genre_list'),
    path('genres/<int:genre_id>/', views.genre_detail, name='genre_detail'),
    path('movies/', views.movie_list, name='movie_list'),
    path('movies/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('movies/<int:movie_id>/reviews/', views.create_review, name='create_review'),
    path('reviews/<int:review_id>/', views.update_or_delete_review, name='update_or_delete_preview'),
] + [
    path('docs/', schema_view.with_ui('redoc'), name='api_docs'),
    path('swagger/', schema_view.with_ui('swagger'), name='api_swagger'),
]
