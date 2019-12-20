### 06 - 프레임워크 기반 웹 페이지 구현

---



#### 1. 데이터베이스

```python
class Movie(models.Model):
    title = models.CharField(max_length=30)
    title_en = models.CharField(max_length=50)
    audience = models.IntegerField()
    open_date = models.DateField()
    genre = models.CharField(max_length=30)
    watch_grade = models.CharField(max_length=30)
    score = models.FloatField()
    poster_url = models.TextField()
    description = models.TextField()


class Review(models.Model):
    content = models.CharField(max_length=150)
    score = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
```



#### 2. 페이지

1. 영화 목록 movie_list.html

```python
{% block body %}
    <img src="{% static 'movie/images/pjt06_movie.jpg' %}" alt="movie" height=200>
    <h1>영화 목록</h1>
    <div>
        <a href="{% url 'movie:new_movie' %}">새 영화 등록</a>
    </div>

    {% if movies %}
    <ul>
        {% for movie in movies %}
            <li>
                <a href="{% url 'movie:movie_detail' movie.id %}">{{ movie.title }}</a> / {{ movie.score }}
            </li>
        {% endfor %}
    </ul>
    {% endif %}
{% endblock body %}
```

2. 영화 정보 생성 forms.py

```python
from django import forms
from .models import Movie, Review

class MovieModelForm(forms.ModelForm):
    title = forms.CharField(min_length=1, max_length=30)
    class Meta:
        model = Movie
        fields = '__all__'


class ReviewModelForm(forms.ModelForm):
    content = forms.CharField(min_length=2, max_length=150)
    class Meta:
        model = Review
        fields = ('content', 'score',)
```

3. 영화 정보 생성 views.py

```python
@require_http_methods(['GET', 'POST'])
def new_movie(request):
    if request.method == 'POST':
        form = MovieModelForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return redirect('movie:detail_movie')

    else:
        form = MovieModelForm()
    return render(request, 'movie/new_movie.html', {
        'form': form,
    })
```

4. 영화 정보 조회 views.py

```python
@require_GET
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    reviews = movie.review_set.all()
    review_form = ReviewModelForm()
    return render(request, 'movie/movie_detail.html', {
        'movie': movie,
        'reviews': reviews,
        'review_form': review_form,
    })
```

5. 영화 정보 수정 _form.html

```python
<form method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="제출">
</form>
```

6. 영화 정보 수정 views.py

```python
@require_http_methods(['GET', 'POST'])
def update_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        form = MovieModelForm(request.POST, instance=movie)
        if form.is_valid():
            movie = form.save()
            return redirect('movie:movie_detail', movie_id)
    else:
        form = MovieModelForm(instance=movie)
    return render(request, 'movie/update_movie.html', {
        'form': form,
    })
```

7. 영화 정보 삭제 views.py

```python
@require_GET
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    reviews = movie.review_set.all()
    review_form = ReviewModelForm()
    return render(request, 'movie/movie_detail.html', {
        'movie': movie,
        'reviews': reviews,
        'review_form': review_form,
    })
```

8. 영화 한줄평 생성 views.py

```python
@require_POST
def new_review(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    form = ReviewModelForm(request.POST)
    if form.is_valid():
        review = form.save(commit=False)
        review.movie_id = movie.id
        review.save()
        return redirect('movie:movie_detail', movie_id)
```



#### 3. 결과

