from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),  # HOST/home// == HOST/home/
    # path('hi/<str:name>/', views.hi),  # HOST/home/hi/
                                       # <str:name> 변수처리
    path('guess/', views.guess, name='guess'),
    path('answer/', views.answer, name='answer'),
]