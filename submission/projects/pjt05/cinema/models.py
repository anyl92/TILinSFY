from django.db import models
from django.urls import reverse


class Movie(models.Model):
    title = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200)
    audience = models.IntegerField()
    open_date = models.DateField()
    genre = models.CharField(max_length=20)
    watch_grade = models.CharField(max_length=20)
    score = models.FloatField()
    poster_url = models.TextField()
    description = models.TextField()

    def get_absolute_url(self):
        return reverse("cinema:movie_detail", kwargs={"movie_id": self.id})