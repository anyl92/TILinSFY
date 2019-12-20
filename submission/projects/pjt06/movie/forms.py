from django import forms
from .models import Movie, Review


class MovieModelForm(forms.ModelForm):
    title = forms.CharField(min_length=1, max_length=30)

    class Meta:
        model = Movie
        fields = '__all__'


class ReviewModelForm(forms.ModelForm):
    content = forms.CharField(min_length=2, max_length=150)

    class Meta:
        model = Review
        fields = ('content', 'score',)