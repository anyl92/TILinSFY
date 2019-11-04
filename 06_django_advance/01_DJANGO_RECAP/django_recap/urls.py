from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('board/', include('board.urls')),
    path('poll/', include('poll.urls')),
    path('home/', include('home.urls')),
]