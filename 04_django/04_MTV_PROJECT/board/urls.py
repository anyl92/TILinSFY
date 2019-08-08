from django.urls import path
from . import views

urlpatterns = [
    # DOMAIN/board/
    # Create
    path('articles/new/', views.new), 
    path('articles/create/', views.create), 
    # Read
    path('articles/', views.index), 
    path('articles/<int:article_id>/', views.show), 
    # Update
    
    # Delete
    path('articles/<int:article_id>/delete/', views.delete), 
]