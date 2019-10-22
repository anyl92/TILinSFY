from django.db import models
from django.urls import reverse
from django.conf import settings


class Posting(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    icon = models.CharField(max_length=30, default='')
    image = models.ImageField(blank=True)  # $ pip install pillow
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at', ]

    def get_absolute_url(self):
        return reverse("sns:posting_detail", kwargs={"posting_id": self.pk})
    
    def __str__(self):
        return f'{self.pk}: {self.content[:20]}'

