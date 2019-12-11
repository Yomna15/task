from django.shortcuts import render, redirect

from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model, login, authenticate

from . import forms

User = get_user_model()

def register(request):
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('email')
            print('username',username)
            name = form.cleaned_data.get('name')
            raw_password = form.cleaned_data.get('password')
            print('pass',raw_password)
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            print('logged in',user)
            return render(request,'registration/sucess_login.html',{'user':user})
    else:
        print('iam in else')
        form = forms.RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

def upload_video(request):
    if request.method == 'POST':
        form = forms.VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = forms.VideoForm()
    return render(request, 'registration/profile.html', {
        'form': form
    })

class ProfileView(TemplateView):
    template_name = 'registration/profile.html'

