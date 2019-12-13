from django.shortcuts import render, redirect
from . import forms

# Create your views here.
def upload_video(request):
    if request.method == 'POST':
        form = forms.VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save()
            print('v',video)
            return render(request,'file_upload/file.html',{'video':video,'test_form':1})
    else:
        form = forms.VideoForm()
    return render(request, 'file_upload/file.html', {
        'form': form,
        'test_form': None
    })
