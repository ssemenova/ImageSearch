from django.contrib.staticfiles.storage import staticfiles_storage
from django.db import connection
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.template import loader

from imagesearch.forms import SearchImagesForm
from imagesearch.models import *

import face_recognition
import pickle

def mainview(request):
    return _mainview_format(request)

def _mainview_format(request, context={}):
    template = loader.get_template('index.html')
    form_search = SearchImagesForm()

    context.update({
        'form_search': form_search,
    })

    return HttpResponse(template.render(context, request))

def upload_image(request):
    if request.method != 'POST':
        return _mainview_format(request)

    query_encoding = _get_face_encoding_for_query(
        request.POST.get('img_input')
    )
    
    known_encodings, IDs = _read_known_encodings_from_pk_files()

    IDs_in_query_image = _get_IDs_in_query_image(
        query_encoding,
        known_encodings,
        IDs
    )

    if IDs_in_query_image:
        selection = request.POST.get('action')
        cursor = connection.cursor()
        formatted_results = []

        if selection == 'select1':                
            query = """SELECT * FROM imagesearch_Person JOIN imagesearch_Address
                    ON imagesearch_Person.AddressID_id = imagesearch_Address.ID
                    JOIN imagesearch_City
                    ON imagesearch_Address.CityID_id = imagesearch_City.ID
                    WHERE imagesearch_Person.ID in (""" + IDs_in_query_image + ")"
            cursor.execute(query)
            query_result = cursor.fetchall()

            for person in query_result:
                formatted_results.append({
                    'name': person[1],
                    'age': person[2], 
                    'email': person[3], 
                    'phone': person[4],
                    'address1': person[9],
                    'address2': person[10],
                    'city': person[13],
                    'state': person[14],
                    'zip': person[15]
                })
        elif (selection == 'select2'):
            query = """SELECT imagesearch_Person.Name, imagesearch_Event.Name
                    FROM imagesearch_Person JOIN imagesearch_EventAttended
                    ON imagesearch_Person.ID = imagesearch_EventAttended.PersonID_id
                    JOIN imagesearch_Event
                    ON imagesearch_EventAttended.EventID_id = imagesearch_Event.ID
                    WHERE imagesearch_Person.ID in (""" + IDs_in_query_image + ")"
            cursor.execute(query)
            query_result = cursor.fetchall()

            names = []

            for qr_item in query_result:
                name = qr_item[0]
                event = qr_item[1]

                if name in names:
                    for fr_item in formatted_results:
                        if fr_item['name'] == name:
                            fr_item['event'].append(event)
                else:
                    formatted_results.append({
                        'name': name,
                        'event': [event]
                    })
                    names.append(name)
        else:
            query = """SELECT DISTINCT(imagesearch_Photo.Filename)
            FROM imagesearch_Person JOIN imagesearch_PhotoOf
            ON imagesearch_Person.ID = imagesearch_PhotoOf.PersonID_id
            JOIN imagesearch_Photo
            ON imagesearch_PhotoOf.PhotoID_id = imagesearch_Photo.ID
            WHERE imagesearch_Person.ID in (""" + IDs_in_query_image + ")"
            cursor.execute(query)
            query_result = cursor.fetchall()

            for image in query_result:
                formatted_results.append(image[0])



    template = loader.get_template('uploadimageresults.html')
    context = {
        'results': formatted_results,
        'querytype': selection,
    }
    return HttpResponse(template.render(context, request))


def _get_face_encoding_for_query(uploaded_file):
    uploaded_image = face_recognition.load_image_file(
        "imagesearch/static/imagesearch/query_images/" + uploaded_file + ".png"
    )

    return face_recognition.face_encodings(uploaded_image)[0]


def _read_known_encodings_from_pk_files():
    encodings = []
    IDs = []
    for p in Person.objects.all():
        path = "imagesearch/static/imagesearch/encodings/" + p.TemplateEncoding
        with open(path, "rb") as f:
            encoding = pickle.load(f)
        encodings.append(encoding)
        IDs.append(p.ID)
    
    return encodings, IDs

    
def _get_IDs_in_query_image(query_encoding, known_encodings, IDs):
    face_recognition_results = face_recognition.compare_faces(
        known_encodings, query_encoding
    )
    IDs_in_photo = filtered_list = [i for (i, v) in zip(IDs, face_recognition_results) if v]
    comma_formatted_IDs = ''.join(str(IDs_in_photo)).strip('[]')

    return comma_formatted_IDs


def search_images(request):
    if request.method == 'POST':
        form = SearchImagesForm(request.POST)
        if form.is_valid():
            cursor = connection.cursor()
            event_ID = form.cleaned_data['query']
            query = """SELECT imagesearch_Photo.Filename 
                        FROM imagesearch_Photo JOIN imagesearch_Event
                        ON imagesearch_Event.ID = imagesearch_Photo.EventID_id
                        WHERE imagesearch_Event.ID = """ + event_ID;
            cursor.execute(query)
            query_result = cursor.fetchall()

            formatted_results = []
            for image in query_result:
                formatted_results.append(image[0])

            event_name = Event.objects.get(ID=event_ID).Name
            template = loader.get_template('searchimageresults.html')

            context = {
                "results": formatted_results,
                "event_name": event_name
            }

            return HttpResponse(template.render(context, request))

