from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    # path('', views.index, name='index'),  # /board/ == board:index
    # read 글 목록(list) render
    path('articles/', views.list, name='list'),
    # read 글 상세(detail) render
    path('articles/<int:id>/', views.detail, name='detail'),

    # create 글쓰기(new) render
    path('articles/new/', views.new, name='new'),
    # create 글 저장(create)
    # path('articles/create/', views.create, name='create'),

    # update 글 수정 쓰기(edit) render
    path('articles/<int:id>/edit/', views.edit, name='edit'),
    # update 글 실제 수정(update)
    # path('articles/<int:id>/update/', views.update, name='update'),

    # delete 글 삭제(delete)
    path('articles/<int:id>/delete/', views.delete, name='delete'),
]
