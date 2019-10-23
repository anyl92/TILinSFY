from django.urls import path
from . import views

app_name = 'postings'

urlpatterns = [
    path('', views.posting_list, name='posting_list'), 
    path('<int:posting_id>/', views.posting_detail, name='posting_detail'), 
    path('create/', views.create_posting, name='create_posting'), 
    path('<int:posting_id>/update/', views.update_posting, name='update_posting'), 
    path('<int:posting_id>/delete/', views.delete_posting, name='delete_posting'), 
    path('<int:posting_id>/comments/create/', views.create_comment, name='create_comment'),
    path('<int:posting_id>/like/', views.toggle_like, name='like'), 
]
