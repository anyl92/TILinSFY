## 05 - Django

1. 기본 설정

```
$ pip install django django_extensions

$ django-admin startproject pjt05 .
$ django-admin startapp cinema

$ mkdir -p cinema/templates/cinema
$ touch cinema/urls.py cinema/forms.py
$ cd cinema/templates/cinema/
$ touch movie_list.html movie_detail.html new_movie.html update_movie.html base.html _form.html
```

django와 extensions를 설치한다. pjt05 프로젝트를 만들고 cinema 앱을 생성한다.

html파일이 들어갈 templates 폴더를 생성하고 하위에 cinema 폴더를 생성한다.

필요한 py파일들과 html파일들을 생성한다.



2. 데이터베이스 생성 (models.py)

```python
from django.db import models
from django.urls import reverse

class Movie(models.Model):
    title = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200)
    audience = models.IntegerField()
    open_date = models.DateField()
    genre = models.CharField(max_length=20)
    watch_grade = models.CharField(max_length=20)
    score = models.FloatField()
    poster_url = models.TextField()
    description = models.TextField()

    def get_absolute_url(self):
        return reverse("cinema:movie_detail", kwargs={"movie_id": self.id})
```

```
$ python manage.py makemigrations cinema
$ python manage.py migrate cinema
```

models.py에서 class를 setting한 후 cinema에 migrate한다.

reverse를 이용해서 url로 만들어 주는 함수를 생성한다.



3. urls.py

```python
from django.urls import path
from . import views

app_name = 'cinema'

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('new/', views.new_movie, name='new_movie'),
    path('<int:movie_id>/update/', views.update_movie, name='update_movie'),
    path('<int:movie_id>/delete/', views.delete_movie, name='delete_movie'),
]
```

각각의 url과 views.*를 연결한다.



4. views.py

```python
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
```

url이 입력되면 연결된 함수로 요청이 들어온다.

요청을 받으면 그 함수에 맞는 html로 응답을 보내준다.

```python
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
```

@require_* 선언된 요청만 받는다.

MovieModelForm을 사용하여 데이터가 제대로 들어왔는지 검증받고, 

데이터베이스에 맞게 HTML파일도 생성된다.

```python
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
```

update 시에는 이전에 저장되었던 내용을 그대로 가져와야 하기 때문에

(instance=movie) 를 사용해준다.



5. forms.py

```python
from django import forms
from .models import Movie


class MovieModelForm(forms.ModelForm):
    title = forms.CharField(min_length=1, max_length=200)

    class Meta:
        model = Movie
        fields = '__all__'
```

forms.ModelForm을 사용하는 부분

데이터를 일일히 입력받지 않아도 한번에 받아준다.



6. html

   1) base.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">

    {% block css %}{% endblock css %}
    <title>{% block title %}{% endblock title %}</title>
</head>
<body>
    {% block body %}
    {% endblock body %}
</body>
</html>
```



​	2) movie_list.html

```html
{% extends 'cinema/base.html' %}

{% block title %} movie list {% endblock %}

{% block body %}
    <h1>This is Movie list</h1>

<div><a href="{% url 'cinema:new_movie' %}">
    <button>새 영화 등록</button></a></div>

{% if movies %}
    <ul>
        {% for movie in movies %}
            <li>
                <a href="{{ movie.get_absolute_url }}">
                {{ movie.title }}</a> {{ movie.score }}
            </li>
        {% endfor %}
    </ul>
{% endif %}

{% endblock body %}
```

a태그의 링크를 눌렀을 때 cinema의 views.py의 new_movie를 호출하여 그때의 url을 받아온다.

movies에 데이터가 있으면 li 내에 영화 제목과 평점을 출력해준다.



​	3) movie_detail.html

```html
{% extends 'cinema/base.html' %}
{% load humanize %}

{% block css %}
<style>
    .ui-button {
        display: inline-block;
    }
</style>
{% endblock css %}
```

load humanize - 숫자에 자동 , 입력 해주는 명령어

css 스타일을 지정해주기 위해 style 선언

```html
{% block title %}Movie detail{% endblock title %}
{% block body %}
    <h3>{{ movie.title }}, {{ movie.title_en }}</h3>
    <p>관객수 : {{ movie.audience|intcomma }}</p>
    <p>개봉일 : {{ movie.open_date }}</p>
    <p>장르 : {{ movie.genre }}</p>
    <p>관람등급 : {{ movie.watch_grade }}</p>
    <p>평점 : {{ movie.score }}</p>
    <img src="{{ movie.poster_url }}" alt="image" width="200">
    <div>{{ movie.description }}</div>
    <br>
    <div>
        <div class="ui-button">
            <a href="{% url 'cinema:movie_list'%}">
                <button>목록</button>
            </a>
        </div>
        <div class="ui-button">
            <a href="{% url 'cinema:update_movie' movie.id %}">
                <button>수정</button>
            </a>
        </div>
        <div class="ui-button">
            <form action="{% url 'cinema:delete_movie' movie.id %}" method="POST">
                {% csrf_token %}
                <input onclick="return confirm('영화 정보가 삭제됩니다.')" type="submit" value="삭제">
            </form>
        </div>
    </div>
{% endblock body %}
```

영화 정보를 표현해준다. 목록, 수정, 삭제는 링크를 연결해서 다른 작업을 할 수 있게 url을 설정해준다.

삭제는 POST요청으로 입력하며 {% csrf_token %}을 입력해주어야 한다.

삭제 요청 시 알림창을 표현해주기 위하여 onclick="return confirm()" 을 사용한다.



​	4) _form.html

```html
<form method="POST">
  {% csrf_token %}
  {{ form.as_p }}
  <input type="submit">
</form>
```



​	5) new_movie.html

```html
{% extends 'cinema/base.html' %}

{% block title %}New Movie{% endblock title %}

{% block body %}
<h1>New Movie</h1>

{% include 'cinema/_form.html' %}

{% endblock body %}
```



​	6) update_movie.html

```html
{% extends 'cinema/base.html' %}

{% block title %}Update movie{% endblock title %}

{% block body %}
<h1>Update movie</h1>

{% include 'cinema/_form.html' %}

{% endblock body %}
```