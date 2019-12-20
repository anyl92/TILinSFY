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
