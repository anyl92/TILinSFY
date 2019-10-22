from django import forms
from .models import Posting, Image


class PostingForm(forms.ModelForm):
    class Meta:
        model = Posting
        fields = ('content', )


class ImageForm(forms.ModelForm):  # 여러개의 사진을 업로드함
    class Meta:
        model = Image
        fields = ('file', )
        widgets = {
            'file': forms.FileInput(attrs={'multiple': True})
        }


# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ('content', )