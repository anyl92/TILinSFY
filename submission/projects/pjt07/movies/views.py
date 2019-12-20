from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.contrib.auth.decorators import login_required

from .models import Movie, Genre, Reviews
from .forms import ReviewModelForm


@require_GET
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movie_list.html', {
        'movies': movies,
    })


@require_GET
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    review_form = ReviewModelForm()
    is_like = movie.like_users.filter(id=request.user.id).exists()
    return render(request, 'movies/movie_detail.html', {
        'movie': movie,
        'review_form': review_form,
        'is_like': is_like,
    })


@login_required
@require_POST
def review_create(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    form = ReviewModelForm(request.POST)
    if form.is_valid():
        review = form.save(commit=False)
        review.movie = movie
        review.user = request.user
        review.save()
    return redirect(movie)


@login_required
@require_POST
def review_delete(request, movie_id, review_id):
    movie = get_object_or_404(Movie, id=movie_id)
    review = get_object_or_404(Reviews, id=review_id)
    if review.user == request.user:
        review.delete()
    return redirect(movie)


@login_required
@require_POST
def like_save(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    user = request.user
    if movie.like_users.filter(id=user.id).exists():
        movie.like_users.remove(user)
    else:
        movie.like_users.add(user)
    return redirect(movie)
