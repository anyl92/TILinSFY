from django.urls import path
from . import views

app_name = 'poll'

urlpatterns = [
    path('questions/<int:question_id>/', views.question_detail, name='question_detail'),
    path('questions/<int:question_id>/upvote', views.upvote, name='upvote'),
]
