from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from .forms import MovieModelForm
from .models import Movie


def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'cinema/movie_list.html', {
        'movies': movies,
    })


def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'cinema/movie_detail.html', {
        'movie': movie,
    })


@require_http_methods(['GET', 'POST'])
def new_movie(request):
    if request.method == 'POST':
        form = MovieModelForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return redirect('cinema:movie_list')
    else:
        form = MovieModelForm()
    return render(request, 'cinema/new_movie.html', {
        'form': form,
    })


@require_http_methods(['GET', 'POST'])
def update_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        form = MovieModelForm(request.POST, instance=movie)
        if form.is_valid():
            movie = form.save()
            return redirect(movie)
    else:
        form = MovieModelForm(instance=movie)
    return render(request, 'cinema/update_movie.html', {
        'form': form,
    })


@require_POST
def delete_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    movie.delete()
    return redirect('cinema:movie_list')