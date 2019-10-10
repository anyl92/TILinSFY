from django import forms
from .models import Article


# Forms.Form => Data 입력 및 검증에 좀 더 치중

# Forms.ModelForm 되게 많은 것을 할 수 있는 핸드폰 케이스라고 생각
# forms.Modelform => Data 입력 / 검증 + HTML 생성

class ArticleModelForm(forms.ModelForm):
    # 1. Data 입력 및 검증
    # 2. HTML 생성
    # title = forms.CharField(min_length=2)
    # title = forms.EmailField(min_length=3, required=False)
    title = forms.CharField(min_length=2, max_length=100)
    
    class Meta:
        model = Article
        fields = '__all__'
