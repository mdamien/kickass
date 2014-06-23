from django.shortcuts import render
from files.models import File
from django import forms
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
import itertools

def file_list(request):
    courses = itertools.groupby(File.objects.filter(hidden=False).select_related(),
                lambda x:x.course.name)
    courses = [(grouper, list(values)) for grouper, values in courses]
    return render(request, 'files/file_list.html', {'courses':courses})

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        exclude = ('user','url', 'hidden')

def upload(request):
    if not request.user.is_authenticated():
        return redirect('{}?next={}'.format(
            reverse('social:begin', args=("google-oauth2",)),
            reverse('files.views.upload')
        ))
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
    file = File.objects.get(pk=file_pk)
    if request.method == 'POST':
        if request.POST['action'] == 'delete':
            if request.user == file.user:
                file.delete()
                return redirect('/')
        else:
            if request.user.is_staff:
                file.hidden = True
                file.save()
    return render(request, 'files/details.html', {'file':file})
