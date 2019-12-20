from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.contrib.auth import login as auth_login, logout as auth_logout, get_user_model
from .forms import CustomUserCreationsForm, CustomUserAuthenticationForm
from .models import User
from movies.models import Reviews


@require_GET
def user_list(request):
    users = User.objects.all()
    return render(request, 'accounts/user_list.html', {
        'users': users, 
    })


@require_http_methods(['GET', 'POST'])
def signup(request):
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
            return redirect('/movies')
    else:
        form = CustomUserAuthenticationForm()
    return render(request, 'accounts/form.html', {
        'form': form,
    })


def logout(request):
    auth_logout(request)
    return redirect('movies:movie_list')


@require_GET
def user_detail(request, user_id):
    user_info = get_object_or_404(User, id=user_id)
    reviews = Reviews.objects.filter(user=user_info)
    return render(request, 'accounts/user_page.html', {
        'user_info': user_info,
        'reviews': reviews,
    })

