from django import forms
from .models import Article, Comment


class ArticleForm(forms.ModelForm):
    # HTML을 어떻게 만들것인지, 검증의 조건
    # 만약 아무것도 적지 않는다면, ModelForm 은 Model을 알고 있기 때문에
    # 각 Model을 읽고 알아서 HTML+검증을 한다
    title = forms.CharField(min_length=2, max_length=200)
    # content에 대하여 어떤 검증/html 관련해서 적지 않아도 -> models.Article의 content 항목을 보고 찾음    
    class Meta:
        model = Article
        # fields 에 적힌 컬럼은 검증 하겠다
        fields = ('title', 'content', )


class CommentForm(forms.ModelForm):
    content = forms.CharField(min_length=2, max_length=200)

    class Meta:
        model = Comment
        fields = ('content',)