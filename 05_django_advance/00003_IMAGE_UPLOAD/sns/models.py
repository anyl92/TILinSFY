from django.db import models
from django.urls import reverse

'''
$ python manage.py migrate <APP_NAME> zero  역순으로 다 지움
$ rm <APP_NAME>/migrations/0*
'''


class Posting(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='like_postings', blank=True)
    content = models.TextField()
    icon = models.CharField(max_length=30, default='')
    image = models.ImageField(blank=True)  # blank : 비어있을수도 있다  
    created_at = models.DateTimeField(auto_now_add=True)  # add : 추가 될 때만
    updated_at = models.DateTimeField(auto_now=True)  # save가 일어날 때 마다

    # Detail 페이지를 쓸 거라면 만들어요.
    def get_absolute_url(self):
        return reverse("sns:posting_detail", kwargs={"posting_id": self.pk})

    def __str__(self):
        return f'{self.pk}: {self.content[:20]}'
