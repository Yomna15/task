from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from . import models
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterForm(UserCreationForm):
    name = forms.CharField(
        required=True,
        label="Name",
        widget=forms.TextInput()
    )
    email = forms.EmailField(
        required=True,
        label="Email",
        widget=forms.EmailInput()
    )
    password = forms.CharField(
        required=True,
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '패스워드',
                'required' : 'True'
            }
        )
    )
    class Meta:
        model = models.User
        fields = ('email','name','password')
        

class VideoForm(forms.ModelForm):
    class Meta:
        model = models.video 
        fields = ('video',)