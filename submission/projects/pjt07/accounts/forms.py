from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreationsForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name',)


class CustomUserAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fiedls = ('username',)