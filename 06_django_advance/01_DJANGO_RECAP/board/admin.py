from django.contrib import admin
from .models import Article

class AritcleAdmin(admin.ModelAdmin):
    list_display = 'ic', 'title'


admin.site.register(Article)
