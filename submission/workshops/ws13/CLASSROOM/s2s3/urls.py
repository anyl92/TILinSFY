from django.urls import path
from . import views

urlpatterns = [
    path('', views.s2s3),
    path('<str:name>/', views.student)
]