from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST
from .models import Article
# from . import models 라고 쓰면 아래에서 models.Article 이라고 써야 하므로


# DB를 조작할 때는 POST, 그냥 받는거는 GET
@require_GET
def index(request):
    return render(request, 'board/index.html')


@require_GET
def list(request):
    articles = Article.objects.all()  # [<A1>, <A2>, A3>, ...]
    # context = {'articles': articles} , return 에 context 넣는거랑 똑같음
    return render(request, 'board/list.html', {
        'articles': articles,
        # context 는 반드시 딕셔너리로 들어감
    })


@require_GET
def detail(request, id):
    # try:
    #     article = Article.objects.get(id=id)
    # except Article.DoesNotExist:
    #     raise Http404(f'Can not find ARTICLE with id {id}')
    # 이렇게 예외처리 하지 말고
    # 아래처럼 쓰면 간단함
    # get_object_or_404 import
    article = get_object_or_404(Article, id=id)
    # 아래 create, update, delete 등에서 다 바꾸기
    return render(request, 'board/detail.html', {
        'article': article,
    })


@require_GET
def new(request):
    return render(request, 'board/new.html')


@require_POST
def create(request):
    article = Article()
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    # 저장한 내용을 detail 에서 볼 것이므로 redirect 를 import
    return redirect('board:detail', article.id)


@require_GET
def edit(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'board/edit.html', {
        'article': article,
    })


@require_POST
def update(request, id):
    article = get_object_or_404(Article, id=id)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    # return redirect('boart/detail.html')
    return redirect('board:detail', article.id)


# post 요청으로 받는 방법
@require_POST
def delete(request, id):
    article = get_object_or_404(Article, id=id)
    article.delete()
    return redirect('board:list')
