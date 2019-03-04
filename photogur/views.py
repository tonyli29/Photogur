from django.http import HttpResponse
from django.shortcuts import render
from photogur.models import Picture, Comment

import datetime

def pics(request):
    context = {
        'pictures': Picture.objects.all()
    }
    response = render(request, 'pictures.html', context)
    return HttpResponse(response)

def picture_show(request, id):
    picture = Picture.objects.get(pk=id)
    comments = picture.comments.all()
    context = {
        'picture': picture,
        'comments': comments
    }
    response = render(request, 'picture.html', context)
    return HttpResponse(response)
