from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from photogur.models import Picture, Comment
from photogur.forms import LoginForm
from django.contrib.auth import authenticate, login, logout

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

def picture_search(request):
    query = request.GET['query']
    search_result = Picture.objects.filter(artist = query)
    context = {
        'pictures': search_result,
        'query': query
    }
    response = render(request, 'search.html', context)
    return HttpResponse(response)

def create_comment(request):
    picture = request.POST['picture']
    comment_name = request.POST['comment_name']
    comment_message = request.POST['comment_message']
    new_comment = Comment.objects.create(name=comment_name, message=comment_message, picture=Picture.objects.get(pk=picture))
    return HttpResponseRedirect('/pictures/' + picture)

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            pw = form.cleaned_data['password']
            user = authenticate(username=username, password=pw)
            if user is None:
                login(request, user)
                return HttpResponseRedirect('/pictures/')
            else:
                form.add_error('username', 'Login failed')
    else:
        form = LoginForm()
    context = {
        'form': form
    }
    response = render(request, 'login.html', context)
    return HttpResponse(response)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/pictures/')

















#
