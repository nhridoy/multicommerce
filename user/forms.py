from django import forms
from user.models import User

from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm


class LoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'px-3 bg-gray-100 py-2 border outline-none w-full my-2', 'placeholder': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'px-3 bg-gray-100 py-2 border outline-none w-full my-2', 'placeholder': 'password'}))

    class Meta:
        model = User
        fields = ['username', 'password']