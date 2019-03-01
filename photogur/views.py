from django.http import HttpResponse
from django.shortcuts import render
from photogur.models import Picture, Comment

import datetime

def pics(request):
    context = {
        'pictures': Picture.objects.all()
    }
    response = render(request, 'picture.html', context)
    return HttpResponse(response)
