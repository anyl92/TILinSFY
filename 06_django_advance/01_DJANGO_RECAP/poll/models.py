from django.db import models
from django.urls import reverse


class Question(models.Model):
    title = models.CharField(max_length=20)
    def get_absolute_url(self):
        return reverse("poll:question_detail", kwargs={"question_id": self.id})

class Choice(models.Model):
    content = models.CharField(max_length=200)
    votes = models.IntegerField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)