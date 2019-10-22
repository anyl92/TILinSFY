from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import User


class CustomUserCreationForm(UserCreationForm):

    class Meta:  # 정보 저장
        model = User
        fields = ('username', 'email',)


class CustomAuthenticationForm(AuthenticationForm):
    
    class Meta:  # 인증
        model = User