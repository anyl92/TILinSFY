from django.shortcuts import render, redirect, get_object_or_404

# user 모델을 가져옴
from django.contrib.auth import get_user_model
# accounts에서 import할 함수
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET, require_POST, require_http_methods

from .models import Article
from .forms import ArticleForm


def like(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    user = request.user
    # if article.like_users.filter(id=user.id).exists():
    if user in article.like_users.all():  # 이미 좋아요 상태
        article.like_users.remove(user)  # 고로 지움
    else:
        article.like_users.add(user)
    return redirect('articles:article_detail', article.id)


@require_GET
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/index.html', {
        'articles': articles,
    })


@require_GET
def article_detail(request, article_id):
    # get_object_or_404 의 1번인자: 모델명, 2번인자: "id=blabla_id"
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'articles/detail.html', {
        'article': article,
    })


@login_required  # CRD는 모두 필요
@require_http_methods(['GET', 'POST'])  # 썼다가 틀릴거 같으면 쓰지마
def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user  # article.user_id = request.user.id
            article.save()
            return redirect('articles:article_detail', article.id)
    else:
        form = ArticleForm()
    return render(request, 'articles/form.html', {
        'form': form,
    })


@login_required  # CRD는 모두 필요
@require_http_methods(['GET', 'POST'])  # 썼다가 틀릴거 같으면 쓰지마
def article_update(request, article_id):
    # Update 추가사항
    # 0. article 하나 찾기
    article = get_object_or_404(Article, id=article_id)
    # 1. User 비교하기
    if article.user != request.user:
        return redirect('articles:article_list')

    if request.method == 'POST':
        # 2. instance 주기
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            # 3. 알아서 하기 (아래 두 줄 코드 날려도 되는데 있어도 큰 문제 없음)
            # 지운다면 form.save() 되야함
            article = form.save(commit=False)
            article.user = request.user  # article.user_id = request.user.id
            article.save()
            return redirect('articles:article_detail', article.id)
    else:
        # 4. 또 instance 주기
        form = ArticleForm(instance=article)
    return render(request, 'article/form.html', {
        'form': form,
    })


@login_required
@require_POST
def article_delete(request, article_id):
    # 주의! user 비교하기
    article = get_object_or_404(Article, id=article_id)
    if request.user != article.user:
        pass
    pass
    