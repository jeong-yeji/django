from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields


class UserForm(UserCreationForm):
    # UserCreationForm은 기본적으로 username, password1, password2를 가지고 있음
    email = forms.EmailField(label='이메일')

    class Meta:
        model = User
        fields = ("username", "email")