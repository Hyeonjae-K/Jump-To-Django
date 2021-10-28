from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    # 이메일 입력검증 필드 추가
    email = forms.EmailField(label='이메일')

    class Meta:
        model = User
        fields = ["username", "password1", "password2", "email"]
