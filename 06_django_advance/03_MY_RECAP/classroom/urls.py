from django.urls import path
from . import views

app_name = 'classroom'

urlpatterns = [
    path('', views.index, name='index'),
    path('students/', views.list, name='list'),
    path('students/new/', views.new, name='new'),

    path('students/create/', views.create, name='create'),
    path('students/<int:id>/', views.detail, name='detail'),
    path('students/<int:id>/edit/', views.edit, name='edit'),
    path('students/<int:id>/update/', views.update, name='update'),
    path('students/<int:id>/delete/', views.delete, name='delete'),
]
