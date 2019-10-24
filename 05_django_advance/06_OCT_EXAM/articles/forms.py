from django import forms
from .models import Article


# forms / models 앞은 s가 붙고, ModelForm / Model 은 안붙는다.
# forms.ModelForm / models.Model
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'content')