from django.shortcuts import render, redirect
from .models import Article

# Create
def new(request):  # 새로운 게시글을 작성할 화면
    return render(request, 'board/new.html')

def create(request):  # 입력 데이터를 DB에 저장
    # request.GET => {'input_title': 제목제목, 'input_content': 내용내용}
    gettitle = request.GET['input_title']
    getcontent = request.GET['input_content']
    
    article = Article.objects.create(title=gettitle, content=getcontent)
    #article.id = article.objects.get(title=gettitle)
    return redirect(f'/board/articles/{article.id}/')

# Read
def index(request):  # 모든 게시글 목록을 보여주는 view
    articles = Article.objects.all()  # []
    return render(request, 'board/index.html', {
        'articles': articles
    })

def show(request, article_id):  # 특정 게시글을 보여주는 view(일)
    article = Article.objects.get(id=article_id)
    return render(request, 'board/show.html', {
        'article': article,
    })

# Update
def edit(request):  # 특정 게시글을 수정할 화면
    return render(request, 'board/edit.html')

# TODO: Delete view 함수 만들기
def delete(request, article_id):  # 특정 게시글을 삭제하는 view
    article = Article.objects.get(id=article_id)
    article.delete()
    return redirect('/board/articles/')