from django.urls import path
from . import views

urlpatterns = [
    path('push/', views.push),
    path('pull/', views.pull),
]