from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from .models import Movie, Review
from .forms import MovieModelForm


def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movie/movie_list.html', {
        'movies': movies,
    })


@require_http_methods(['GET', 'POST'])
def new_movie(request):
    if request.method == 'POST':
        form = MovieModelForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return redirect('movie:movie_detail')  # url로 redirect
    else:
        form = MovieModelForm()
    return render(request, 'movie/new_movie.html', {
        'form': form,
    })


def movie_detail(request, movie_id):
    return