from django import forms
from .models import Movie, Genre, Reviews

class ReviewModelForm(forms.ModelForm):
    
    class Meta:
        model = Reviews
        fields = ("content", "score", )