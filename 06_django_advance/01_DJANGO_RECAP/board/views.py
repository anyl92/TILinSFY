from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from .forms import ArticleModelForm
from .models import Article

from IPython import embed

# CRUD
@require_http_methods(['GET', 'POST'])
def new(request):
    # 요청이 GET/POST 인지 확인한다.
    # 만약 POST라면
    if request.method == 'POST':
        # ArticleModelForm 의 인스턴스를 생성하고 Data 를 채운다(binding).
        form = ArticleModelForm(request.POST)

        # embed()  # 여기서 코드를 멈춤, shell에 작성하는 코드랑 이어 나감

        # binding 된 form 이 유효한지 체크한다.
        if form.is_valid():
            # 유효하다면 저장한다.
            article = form.save()  # form 이 아니고 실제 알맹이인 article 이 save
            # 저장한 article 로 redirect 한다.
            return redirect(article)
        # # form 이 유효하지 않다면,
        # else:
        #     # 유효하지 않은 입력데이터를 담은 HTML과 에러메세지를 사용자에게 보여준다.
        #     return render(request, 'board/new.html', {
        #         'form': form,
        #     })
    # GET 이라면
    else:
        # 비어있는 form(html 생성기) 을 만든다.
        form = ArticleModelForm()  # html 좀 만들어줘
    # form 과 html 을 사용자에게 보여준다.
    return render(request, 'board/new.html', {
        'form': form,
    })

def list(request):
    articles = Article.objects.all()
    return render(request, 'board/list.html', {
        'articles': articles,
    })

def detail(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'board/detail.html', {
        'article': article,
    })


@require_http_methods(['GET', 'POST'])
def edit(request, id):
    article = get_object_or_404(Article, id=id)

    if request.method == 'POST':
        form = ArticleModelForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect(article)
    else:
        # 이전 데이터를 받아와서 그대로 사용할거야
        form = ArticleModelForm(instance=article)
    return render(request, 'board/edit.html', {
        'form': form,
    })


@require_POST
def delete(request, id):
    article = get_object_or_404(Article, id=id)
    article.delete()
    return redirect('board:list')
