from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout


@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:  # login 함?
        return redirect('/')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # 회원 DB에 저장 완료
            auth_login(request, user)  # 인증 시작
            return redirect('/')

    else:
        form = UserCreationForm()
    
    return render(request, 'accounts/signup.html', {
        'form': form,
    })


@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:  # login 한 사용자가 또 로그인을?
        return HttpResponse(content='또 로그인을?', status=400)

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        # 첫번째 인자는 보통 데이터인데 얘만 request가 들어간다
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)  # login 시작 (인증됨)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {
        'form': form
    })


def logout(request):
    auth_logout(request)
    return redirect('/')