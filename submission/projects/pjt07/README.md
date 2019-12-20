# Project 07 - 데이터베이스 설계 | 191101

TEAM : 안유림, 최솔지, 홍수경



## 00_기본설정

1. django project 와 app 생성

   `python django-admin startproject pjt07`

   `python django-admin startapp movies`

   `python django-admin startapp accounts`

   

2. settings.py 설정

* `INSTALLED_APPS` list 에 'accounts' , 'movies', django_extensions' 추가 
* `LANGUAGE_CODE` 를  'ko-kr' 로 설정 변경



4. `pjt.06` 의 `urls.py` 에서 path 추가 
   * `urlpatterns` 에 ` path('movies/', include('movies.urls'))` , `path('accounts/', include('accounts.urls'))`추가하여 movoies App, accounts App 과 연결하기 



## 01_데이터 베이스 생성

1. movies app `models.py`

   ```python
   from django.db import models
   from django.urls import reverse
   from django.conf import settings
   
   class Genre(models.Model):
       name = models.CharField(max_length=200)
   
   class Movie(models.Model):
       title = models.CharField(max_length=200)
       audience = models.IntegerField()
       poster_url = models.CharField(max_length=200)
       description = models.TextField()
       genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
   	like_users = models.ManyToManyField(settings.AUTH_USER, realted_ name='like_movies')
   
       def get_absolute_url(self):
           return reverse("movies:movie_detail", kwargs={"movie_id": self.pk})
   
   class Reviews(models.Model):
       content = models.CharField(max_length=200)
       score = models.IntegerField()
       movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
       user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
   
   ```

   * `get_absolute_url(self)` 

     * `movie_detail.html` 을 자주 사용하기 때문에 함수로 설정
   * `like_users` 
     * ManyToManyField 를 통해 N 대 M 으로 연결

   

2. accounts app `models.py`

```python
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    email = models.EmailField(max_length=200, blank=True, default='')
    first_name = models.CharField(max_length=30, blank=True, default='')
    last_name = models.CharField(max_length=30, blank=True, default='')
```



## 02_ Seed Data 반영 

제공된 README 에 적힌 명령어를 통해 movie.json 과 genre.json 파일 데이터 베이스에 반영 



## 03_ `accounts` App

마스터 APP 에서 `AUTH_USER_MODEL = 'accounts.User'`을 설정하고 시작한다.

accounts db 를 위한 모델을 생성한다. 명세에서 email, first_name, last_name 은 선택 필드로 주어지므로, 

``````python
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    email = models.EmailField(max_length=200, blank=True, default='')
    first_name = models.CharField(max_length=30, blank=True, default='')
    last_name = models.CharField(max_length=30, blank=True, default='')
``````

`block=True` 값을 주어 빈칸으로도 form 작성이 가능하게 한다.

아래 form 은 views 에서 signup/login 을 위해 사용할 것이다.

``````python
class CustomUserCreationsForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name',)
        # 회원가입 시에 username, email, fiset_name, last_name 이 필요하지만 (뒤의 세개는 선택사항)


class CustomUserAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fiedls = ('username',)
        # 로그인 시에는 username 과 password 로만 로그인할 수 있도록 form 을 새로 만든다.
``````

- signup / login / logout

``````python
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.contrib.auth import login as auth_login, logout as auth_logout, get_user_model
from .forms import CustomUserCreationsForm, CustomUserAuthenticationForm
# UserCreationForm, UserAuthenticationsForm 이 아니라, 직접 forms 에서 만든 custom form 을 import 한다.
from .models import User

@require_http_methods(['GET', 'POST'])
def signup(request):
    # 로그인이 되어있을 경우, 영화 리스트 페이지로 이동한다. 
    if request.user.is_authenticated:
        return redirect('/movies')
    
    if request.method == 'POST':
        form = CustomUserCreationsForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('/movies')
    else:
        form = CustomUserCreationsForm()
    return render(request, 'accounts/form.html', {
        'form': form,
    })


@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('/movies')
    
    if request.method == 'POST':
        form = CustomUserAuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            # 로그인은 회원가입과 유사하지만 인자가 두 개인 부분에 주의해서 만들었다.
            return redirect('/movies')
    else:
        form = CustomUserAuthenticationForm()
    return render(request, 'accounts/form.html', {
        'form': form,
    })


def logout(request):
    auth_logout(request)
    return redirect('movies:movie_list')
``````

- detail

``````python
from movies.models import Reviews
# review 를 가져오기 위해 movies 폴더에서 Reviews 모델을 가져온다.

@require_GET
def user_detail(request, user_id):
    # user 가 가지고 있는 정보를 받아온다.
    user_info = get_object_or_404(User, id=user_id)
    # reviews 들을 가져와서, 해당하는 user 가 작성한 review 만 필터링한다.
    reviews = Reviews.objects.filter(user=user_info)
    return render(request, 'accounts/user_page.html', {
        'user_info': user_info,
        'reviews': reviews,
    })
``````

웹브라우저에 출력되는 html 모습은 아래와 같다.

movies 에서 작성하는 like, review 기능은 user_id 로 가져올 수 있다.

``````django
{% extends 'base.html' %}

{% block body %}
    <h5>Like Movies ♥</h5>
    <hr></hr>
	<!-- user_info 에서 '좋아요'를 누른 영화들을 전부 가져와서 for문 안에서 출력한다. -->
    {% for movie in user_info.like_movies.all  %}
        <li>
		<!-- 이 때, 영화 제목을 클릭하면 detail 로 연결하는 링크를 추가했다. -->
            <a style="text-decoration: none" href="{% url 'movies:movie_detail' movie.id %}">{{ movie.title }}</li></a>
    {% endfor %}
	<!-- reviews 는 따로 받아온다. -->
    <h5>Reviews ♥</h5>
    {% for review in reviews %}
        <li>{{ review.movie.title}}:  {{ review.content }} ({{ review.score }})</li></a>
    {% endfor %}
    <hr>
{% endblock body %}
``````

이때, `base.html` 은 마스터 APP 의 TEMPLATES 경로에`'DIRS': [os.path.join(BASE_DIR,'templates')]` 를 추가해서 project 폴더에 있는 templates 의 `base.html`을 가져왔다.

`base.html` 을 작성할 때는, STATIC 경로를 설정해서 css 파일을 가져온다.

![pjt07_static](.\images\pjt07_static.PNG)

- user list 

  users 를 전부 받아서 for문을 돌며 출력한다.

``````django
{% block body %}
    <ul class="list-group list-group-flush">
        {% for user in users %}
            <li class="list-group-item">
                <a style="text-decoration: none" href="{% url 'accounts:user_detail' user.id %}">
                    {{ user.username }}
                </a>
                <!-- username 이 화면에 보이고, 클릭하면 user_page로 연결한다. a 태그에 기본으로 있는 밑줄을 제거하는 부분을 추가했다. -->
            </li>
        {% endfor %}
    </ul>
{% endblock body %}
``````



## 04_ `movies` App

1. `urls.py` 

```python
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
```



2. `views.py` import 함수 

```python
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.contrib.auth.decorators import login_required

from .models import Movie, Genre, Reviews
from .forms import ReviewModelForm
```



3. `forms.py` 

```python
from django import forms
from .models import Movie, Genre, Reviews

class ReviewModelForm(forms.ModelForm):
    
    class Meta:
        model = Reviews
        fields = ("content", "score", )
```

* review_create 함수 작용시 편리하게 ReviewModelForm 사용하기 위해 생성



4. movie_list 함수

```python
@require_GET
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movie_list.html', {
        'movies': movies,
    })
```



5. movie_detail 함수 

```python
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

```

* movie_detail.html 에서 review 작성과 내용 제공 및 좋아요 구현 실행하기 위해
  * ` ReviewModelForm()` , `movie.like_users.filter(id=request.user.id).exists()` 사용



6. review_create 함수 

```python
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
```

* `ReviewModelForm(request.POST)` 를 통해서 해당 movie 에 작성된 review 를 불러온다. 
* form 유효성 검사를 통해 저장한다. 
* movie_id 와 user 는 user가 작성할 수 없기 때문에 `commit=False` 를 통해서 제어한 후 movie_id 와 user 를 설정하여 저장한다. 



7. review_delete 함수

```python
@login_required
@require_POST
def review_delete(request, movie_id, review_id):
    movie = get_object_or_404(Movie, id=movie_id)
    review = get_object_or_404(Reviews, id=review_id)
    if review.user == request.user:
        review.delete()
    return redirect(movie)
```

* movie 를 설정한 후 해당 movie 의 특정 review 를 삭제 
* 만약 review 의 user 가 요청하는 user 일 경우에만 해당 review 삭제 가능하게 설정 



8. like_save 함수

```python
@login_required
@require_POST
def like_save(request, movie_id, review_id):
    movie = get_object_or_404(Movie, id=movie_id, review_id=review_id)
    user = request.user
    if movie.like_users.filter(id=user.id).exists():
        movie.like_users.remove(user)
    else:
        movie.like_users.add(user)
    return redirect(movie)
```

* `if movie.like_users.filter(id=user.id).exists():` 
  * 만약 해당 movie 에 이미 user 가 좋아요를 실행했을 경우 user 를 제거하고 그렇지 않으면 user 를 추가한다. 



9. movie_list.html

```html
{% extends 'base.html' %}
{% block body %}

<div>
    {% for movie in movies %}
    <a href="{% url 'movies:movie_detail' movie.id %}">
        <img src="{{ movie.poster_url }}" alt="{{ movie.title }}" style="width: 120px; height: auto;">
    </a>
    {% endfor %}
</div>

{% endblock body %}
```

movie model 에서 받아온 poster_url로 movie_list를 표현했고, link를 걸어서 movie.id에 맞는 movie_detail로 이동할 수 있게 구성하였습니다.



10. movie_detail.html

```html
{% extends 'base.html' %}
{% load bootstrap4 %}
{% load humanize %}

{% block title %}{% endblock title %}
{% block body %}

<div class="card mb-3" style="max-width: 5000px;">
  <div class="row no-gutters">
    <div class="col-md-4">
      <img src="{{ movie.poster_url }}" alt="{{ movie.title }}" style="width: 300px;" />
    </div>

    <div class="col-md-8">
      <div class="card-body">
        <div>
          <h5 class="card-title" style="display:inline;">{{ movie.title }}</h5>
          <form action="{% url 'movies:like_save' movie.id %}" method="POST" style="display:inline;">
            {% csrf_token %}
            <button style="border: 0; background: none;">
              {% if is_like %}
              <i class="fas fa-heart fa-lg" style="color:#ed4956"></i>
              {% else %}
              <i class="far fa-heart fa-lg" style="color:black;"></i>
              {% endif %}
            </button>
          </form>
        </div>

        <p class="card-text">
          <p>누적 관객수 : {{ movie.audience|intcomma }} | 장르 : {{ movie.genre.name }}</p>
          <p>{{ movie.description }}</p>
        </p>

        <div class="card-text"><small class="text-muted">
            <ul>
              {% for review in movie.reviews_set.all %}
              <li>
                <div>
                  <strong>{{ review.user }}: </strong>
                  {{ review.content }} ({{ review.score }})

                  {% if user == review.user %}
                  <form style="display:inline;" action="{% url 'movies:review_delete' movie.id review.id %}"
                    method="POST">
                    {% csrf_token %}
                    <button style="padding:0; border:none; background:none;">
                      <i class="fas fa-trash"></i>
                    </button>
                  </form>
                </div>
                {% endif %}
              </li>
              {% endfor %}
            </ul>
          </small></div>

      {% if request.user.is_authenticated %}
      <form method="POST" action="{% url 'movies:review_create' movie.id%}">
        {% csrf_token %}
        {% bootstrap_form review_form %}
        {% buttons %}
        <button class="btn btn-info">제출</button>
        {% endbuttons %}
      </form>
      {% endif %}
    </div>
  </div>
</div>
</div>
</div>
{% endblock body %}
```

detail page에 영화의 상세 정보를 표현했습니다.

로그인 된 상태에서 평점 댓글을 달 수 있게 로그인 안 된 유저에게는 평점이 보이지 않게 구성했습니다.

평점은 평점을 단 유저만 삭제할 수 있게 조건을 걸어줬습니다.

좋아요 하트 버튼을 누르면 마이페이지에 좋아하는 영화 리스트가 나오도록 구성했습니다.



## 05_후기

* 유림

  * git 을 활용한 프로젝트 방법을 익히게 되었다.
  * 직접 프로젝트를 해봄으로써 웹 페이지 구성의 흐름과 django 이해에 도움이 되었다.
  * 팀 프로젝트로 시너지를 내서 웹 페이지가 예쁘게 잘 완성되어 뿌듯하다.

* 솔지

  * 처음으로 git 을 활용한 팀 프로젝트를 하면서, 너무 갈등이 없어 나중에 힘들어질까봐 걱정될 정도로 안정적인 팀이었습니다.
  * 각각 팀원들이 가지고 있는 목표가 동일하여 함께 동기부여해서 수행할 수 있던게 가장 큰 이점이었다고 생각합니다.
  * 부족한 부분을 채워주고, 서로 기다려주며 좋은 결과물을 낼 수 있었습니다.

* 수경

  * 첫 팀프로젝트를 통해 github을 많이 활용할 수 있었습니다. 

  * 다른 팀과 달리 3인으로 구성되어 git push & git pull 과정에서 많은 충돌을 걱정했지만 걱정과 달리 진행이 순조러웠습니다. 

  * 팀원들과 코딩분담?이 적절했고 서로 도와가면서 화기애애♥ 하게 프로젝트를 진행하여 추가적으로 bootstrap 까지 진행할 수 있었습니다. 

    