from rest_framework import serializers
from .models import Genre, Movie, Review


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    content = serializers.CharField(label="Content of Review")
    score = serializers.IntegerField(min_value=1, max_value=5, label='Score')
    class Meta:
        model = Review
        fields = ('content', 'score',)