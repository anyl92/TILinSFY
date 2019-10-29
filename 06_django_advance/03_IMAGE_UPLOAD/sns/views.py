from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST
from django.contrib.auth.decorators import login_required

from .models import Posting
from .forms import PostingModelForm


@require_GET
def posting_list(request):
    # nickname = request.COOKIES.get('nickname')
    postings = Posting.objects.all()
    return render(request, 'sns/posting_list.html', {
        'postings': postings,
        # 'nickname': nickname,
    })


# @login_required
@require_GET
def posting_detail(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    comments = posting.comments.all()   # related name 때문 ( 없으면 posting.comment_set.all() )
    if posting.like_users.filter(id=request.user.id).exists():
        is_like = True 
    else:
        is_like = False
    return render(request, 'sns/posting_detail.html', {
        'posting': posting,
        'comments': comments,
        'is_like': is_like,
    })


# @login_required
@require_POST
def create_posting(request):
    # form = PostingModelForm()  # () == 아무 내용 없는 modelform 생성 / (request.POST) == post 요청 내용을 검증&저장 준비
    form = PostingModelForm(request.POST, request.FILES)  # image 를 FILES 로 받았기 때문에 따로 받아야 함
    if form.is_valid():  # 검증
        posting = form.save(commit=False)  # 저장 > Posting 객체를 return
        # posting.user_id = request.user.id
        posting.user = request.user  # user 객체로 맵핑 가능
        # anonymous 라면? > login_required 때문에 불가능
        posting.save()
        return redirect(posting)  # 성공하면 detail page
    else:
        return redirect('sns:posting_list')  # 실패하면 list page