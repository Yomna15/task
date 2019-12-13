from django import forms
from . import models

class VideoForm(forms.ModelForm):
    class Meta:
        model = models.video 
        fields = ('video',)