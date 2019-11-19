from django.urls import path
from . import views

app_name = 'todos'  # 필요없음..

urlpatterns = [
    path('', views.create_todo),
    # PATCH api/v1/todos/1 => Update 1 || DELETE api/v1/todos/1 => Delete 1
    path('<int:todo_id>/', views.update_delete_todo),
    
]
