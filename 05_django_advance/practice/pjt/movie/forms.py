from django import forms
from .models import Movie, Review


class MovieModelForm(forms.ModelForm):
    title = forms.CharField(min_length=1, max_length=30)

    class Meta:
        model = Movie
        fields = '__all__'
