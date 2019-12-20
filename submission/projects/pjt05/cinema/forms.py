from django import forms
from .models import Movie


class MovieModelForm(forms.ModelForm):
    title = forms.CharField(min_length=1, max_length=200)

    class Meta:
        model = Movie
        fields = '__all__'