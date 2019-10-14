from django import forms
from .models import Article, Comment


# Forms.Form => Data 입력 및 검증 + HTML 제공 -> Model 정보 모름

# Forms.ModelForm 되게 많은 것을 할 수 있는 핸드폰 케이스라고 생각
# forms.Modelform => Data 입력 및 검증 + HTML 제공 -> Model 정보 앎

class ArticleForm(forms.Form):
    title = forms.CharField(min_length=2, max_length=100)
    content = forms.CharField()


class ArticleModelForm(forms.ModelForm):
    # 1. Data 입력 및 검증
    # 2. HTML 생성
    # title = forms.CharField(min_length=2)
    # title = forms.EmailField(min_length=3, required=False)
    title = forms.CharField(min_length=2, max_length=100)
    
    class Meta:
        model = Article
        fields = '__all__'


class CommentModelForm(forms.ModelForm):
    content = forms.CharField(min_length=2, max_length=200)  # 200 을 검증

    class Meta:
        model = Comment
        fields = ('content', )  # content만
        # fields = '__all__' 모두