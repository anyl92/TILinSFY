from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('<int:article_id>/', views.article_detail, name='article_detail'),
    path('create/', views.article_create, name='article_create'),
    path('<int:article_id>/update/', views.article_update, name='article_update'),
    path('<int:article_id>/delete/', views.article_delete, name='article_delete'),
    path('<int:article_id>/like/', views.like, name='like'),
 ]