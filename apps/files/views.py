from django.shortcuts import render
from files.models import File
from django import forms
from django.shortcuts import redirect
import itertools

def file_list(request):
    courses = itertools.groupby(File.objects.all().select_related(),
                lambda x:x.course.name)
    courses = [(grouper, list(values)) for grouper, values in courses]
    return render(request, 'files/file_list.html', {'courses':courses})

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        exclude = ('user',)

def upload(request):
    form = FileForm()
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            file.user = request.user
            file.save()
            return redirect(file)
    return render(request, 'files/upload.html', {'form':form})

def details(request, file_pk):
    return render(request, 'files/details.html',
                    {'file':File.objects.get(pk=file_pk)})
