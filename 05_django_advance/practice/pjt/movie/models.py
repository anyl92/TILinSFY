from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=30)
    title_en = models.CharField(max_length=50)
    audience = models.IntegerField()
    open_date = models.DateField()
    genre = models.CharField(max_length=30)
    watch_grade = models.CharField(max_length=30)
    score = models.FloatField()
    poster_url = models.TextField()
    description = models.TextField()


class Review(models.Model):
    content = models.CharField(max_length=150)
    score = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
