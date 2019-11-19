from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup),
    path('my_todos/', views.my_todos),
]
