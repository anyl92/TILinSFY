## 08 - REST API



#### 01 기본 설정, 데이터베이스 설계

pjt08/urls.py

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('movies.urls')),
]
```



movies/urls.py

```python
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
```



models.py

```python
from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    audience = models.IntegerField()
    poster_url = models.CharField(max_length=200)
    description = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)


class Review(models.Model):
    content = models.CharField(max_length=200)
    score = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
```



#### 02 Seed Data 반영

```bash
$ python manage.py loaddata genre.json
$ python manage.py loaddata movie.json
```



admin.py

```python
from django.contrib import admin
from .models import Movie, Genre 

admin.site.register(Movie)
admin.site.register(Genre)
```



#### 03 `movies` API

serializers.py

```python
from rest_framework import serializers
from .models import Genre, Movie, Review


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    content = serializers.CharField(label="Content of Review")
    score = serializers.IntegerField(min_value=1, max_value=5, label='Score')
    class Meta:
        model = Review
        fields = ('content', 'score',)
```



views.py

```python
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Genre, Movie, Review
from .serializers import GenreSerializer, MovieSerializer, ReviewSerializer


@api_view(['GET'])
def genre_list(request):
    genres = Genre.objects.all()
    genres_serializer = GenreSerializer(genres, many=True)
    return Response(genres_serializer.data)


@api_view(['GET'])
def genre_detail(request, genre_id):
    genre = get_object_or_404(Genre, id=genre_id)
    genre_serializer = GenreSerializer(genre)
    return Response(genre_serializer.data)


@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    movies_serializer = MovieSerializer(movies, many=True)
    return Response(movies_serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    movie_serializer = MovieSerializer(movie)
    return Response(movie_serializer.data)


@api_view(['POST'])
def create_review(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    review_serializer = ReviewSerializer(data=request.data)
    if review_serializer.is_valid(raise_exception=True):
        review_serializer.save(movie=movie)
    return Response({'message': '작성되었습니다'})


# @api_view(['PUT','DELETE'])
@api_view(['PATCH','DELETE'])
def update_or_delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if request.method == 'PATCH':
        review_serializer = ReviewSerializer(data=request.data, instance=review)
        if review_serializer.is_valid(raise_exception=True):
            review_serializer.save()
            return Response({'message': '수정되었습니다.'})
    else:
        review.delete()
        return Response({'message': '삭제되었습니다.'})
```