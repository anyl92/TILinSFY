from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import login as auth_login, logout as auth_logout
# user 모델을 가져옴
from django.contrib.auth import get_user_model
# accounts에서 import할 함수
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required


# @require_http_methods[('GET', 'POST')]
def signup(request):
    if request.user.is_authenticated:
        return redirect('article:article_list')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # 로그인을 하도록 합시다 인자가 두개
            auth_login(request, user)
            # 나는 못해요 ..
            # return redirect('articles:article_list')
            # 나는 할수 있어요!
            return redirect(request.GET.get('next') or 'articles:article_list')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/form.html', {
        'form':form,
    })


def login(request):
    if request.user.is_authenticated:
        return redirect('article:article_list')

    if request.method == 'POST':
        # AuthenticationForm 은 인자가 2(request, request.POST)개
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # 로그인 성공 -> 성공한 user를 꺼낸다
            user = form.get_user() 
            auth_login(request, user)
            return redirect('articles:article_list')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/form.html', {
        'form':form,
    })

def logout(request):
    # auth_logout 은 인자 1개
    auth_logout(request)
    return redirect('articles:article_list')