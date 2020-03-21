from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.template import loader

from .forms import UploadImageForm, SearchImagesForm

import face_recognition

def mainview(request):
    template = loader.get_template('index.html')
    form_upload = UploadImageForm()
    form_search = SearchImagesForm()

    context = {
        'form_upload': form_upload,
        'form_search': form_search,
    }

    return HttpResponse(template.render(context, request))

def upload_image(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            template = loader.get_template('uploadimageresults.html')

            context = {
            }

            return HttpResponse(template.render(context, request))


def search_images(request):
    if request.method == 'POST':
        form = SearchImagesForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            template = loader.get_template('searchimageresults.html')

            context = {
            }

            return HttpResponse(template.render(context, request))

