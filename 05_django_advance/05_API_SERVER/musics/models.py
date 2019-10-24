from django.db import models


class Artist(models.Model):
    name = models.TextField()


class Music(models.Model):
    title = models.TextField()
    artist = models.ForeignKey(Artist, on_delete=models.DO_NOTHING)


class Comment(models.Model):
    music = models.ForeignKey(Music, on_delete=models.CASCADE)
    content = models.TextField()