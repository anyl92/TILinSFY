from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    # path('', views.index, name='index'),  # /board/ == board:index
    # read 글 목록(list) render
    path('articles/', views.article_list, name='article_list'),
    # read 글 상세(detail) render
    path('articles/<int:article_id>/', views.article_detail, name='article_detail'),

    # create 글쓰기(new) render
    path('articles/new/', views.new_article, name='new_article'),
    # create 글 저장(create)
    # path('articles/create/', views.create, name='create'),

    # update 글 수정 쓰기(edit) render
    path('articles/<int:article_id>/edit/', views.edit_article, name='edit_article'),
    # update 글 실제 수정(update)
    # path('articles/<int:id>/update/', views.update, name='update'),

    # delete 글 삭제(delete)
    path('articles/<int:article_id>/delete/', views.delete_article, name='delete_article'),

    # Comment Create
    path('articles/<int:article_id>/comments/new/', views.new_comment, name='new_comment'),
]
