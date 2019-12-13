from django.shortcuts import render, redirect

from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model, login, authenticate

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from . import forms
from . import serializers

User = get_user_model()

def register(request):
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('email')
            name = form.cleaned_data.get('name')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request,'registration/sucess_login.html',{'user':user})
    else:
        print('iam in else')
        form = forms.RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

class ProfileView(TemplateView):
    template_name = 'registration/profile.html'

class RegisterAPIView(APIView):
    def post(self, request):
        print('name',request.data['name'])
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data},status=status.HTTP_201_CREATED)
        return Response({'details':serializer._errors},status=status.HTTP_400_BAD_REQUEST)